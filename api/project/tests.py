from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.test import TestCase

from timeSync.models import TimeSync
from project.models import Project
from sheet.models import Sheet
from project import services
import datetime
import json

User = get_user_model()

# store the password to login later
password = 'mypassword'


# Create your tests here.
class BasicTests(TestCase):

    def login(self):
        if not hasattr(self, 'user'):
            self.user = User.objects.create_superuser('myuser', 'myemail@test123.com', password)
        if not hasattr(self, 'user_other'):
            self.user_other = User.objects.create_superuser('other', 'other@test123.com', password)

        self.client = APIClient()
        self.client.login(email=self.user.email, password=password)

    def login_other(self):
        self.client = APIClient()
        self.client.login(email=self.user_other.email, password=password)

    def setUp(self):
        self.login()

    def test_project_create_and_base_sheet(self):
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'url': 'test'}
        response = self.client.post('/api/project/', project_data, format='json')
        response_data = json.loads(response.content)['data']
        self.assertEqual(response.status_code, 200)
        self.assertEquals(json.loads(response.content)['status'], 'success')
        self.assertTrue(response_data['id'] > 0)
        self.assertEquals(response_data['owner'], self.user.id)
        self.assertEquals(response_data['name'], project_data['name'])
        self.assertEquals(response_data['meta'], project_data['meta'])
        self.assertTrue(len(str(response_data['createdAt'])) > 5)
        self.assertTrue(len(str(response_data['updatedAt'])) > 5)
        self.assertIsNone(response_data['deletedAt'])
        self.assertEqual(Sheet.objects.filter(project=response_data['id']).count(), 1)

    def test_deny_projects_when_not_logged_in(self):
        self.client.logout()
        response = self.client.get('/api/project/', format='json')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/api/project/1/', format='json')
        self.assertEqual(response.status_code, 403)

    def test_can_only_see_own_projects(self):
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'owner': self.user, 'url': 'test'}
        project_data_other = {'name': 'testProject', 'meta': 'meta items here', 'owner': self.user_other, 'url': 'test'}

        user_project = Project.objects.create(**project_data)
        user_other_project = Project.objects.create(**project_data_other)

        # // make sure 2 projects exist
        self.assertEqual(Project.objects.all().count(), 2)

        response = self.client.get(f'/api/project/{user_project.id}/', format='json')
        self.assertEqual(response.status_code, 200)

        response_other = self.client.get(f'/api/project/{user_other_project.id}/', format='json')
        self.assertEqual(response_other.status_code, 404)

    def test_project_service_sheets_based_on_3_dates(self):
        """ Test timing of sheets returns correctly
        (x1) of x3 sheets (past, today. future) """

        projectServiceIns = services
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'owner': self.user, 'url': 'test'}

        past_date = datetime.date.today() - datetime.timedelta(days=6)
        future_date = datetime.date.today() + datetime.timedelta(days=6)

        user_project = Project.objects.create(**project_data)

        user_sheet_past = Sheet.objects.create(project=user_project, owner=self.user, meta='past')
        user_sheet_today = Sheet.objects.create(project=user_project, owner=self.user, meta='today')
        user_sheet_future = Sheet.objects.create(project=user_project, owner=self.user, meta='future')

        TimeSync.objects.create(sheet=user_sheet_past, owner=self.user, durationVal=1, durationType='DY', date=past_date, meta=user_sheet_past.meta)
        TimeSync.objects.create(sheet=user_sheet_today, owner=self.user, durationVal=1, durationType='DY', meta=user_sheet_today.meta)
        TimeSync.objects.create(sheet=user_sheet_future, owner=self.user, durationVal=1, durationType='DY', date=future_date, meta=user_sheet_future.meta)

        result = projectServiceIns.collect_sheets_by_rank(user_project)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, user_sheet_today.id)
        self.assertEqual(result[0].meta, user_sheet_today.meta)
        self.assertEqual(result[0].project, user_sheet_today.project)

    def test_project_service_sheets_returns_correct(self):
        """ Test timing of sheets returns correctly (x2) of x3 sheets
        (past, today. future) based on the overlap of time and ranking"""

        projectServiceIns = services
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'owner': self.user, 'url': 'test'}

        past_date = datetime.date.today() - datetime.timedelta(days=6)
        future_date = datetime.date.today() + datetime.timedelta(days=6)

        user_project = Project.objects.create(**project_data)

        user_sheet_past = Sheet.objects.create(project=user_project, owner=self.user, meta='past', ranking=1)
        user_sheet_today = Sheet.objects.create(project=user_project, owner=self.user, meta='today', ranking=10)
        user_sheet_future = Sheet.objects.create(project=user_project, owner=self.user, meta='future', ranking=100)

        TimeSync.objects.create(sheet=user_sheet_past, owner=self.user, durationVal=10, durationType='DY', date=past_date, meta=user_sheet_past.meta)
        TimeSync.objects.create(sheet=user_sheet_today, owner=self.user, durationVal=10, durationType='DY', meta=user_sheet_today.meta)
        TimeSync.objects.create(sheet=user_sheet_future, owner=self.user, durationVal=10, durationType='DY', date=future_date, meta=user_sheet_future.meta)

        result = projectServiceIns.collect_sheets_by_rank(user_project)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, user_sheet_past.id)
        self.assertEqual(result[0].meta, user_sheet_past.meta)
        self.assertEqual(result[0].project, user_sheet_past.project)
        self.assertEqual(result[1].id, user_sheet_today.id)
        self.assertEqual(result[1].meta, user_sheet_today.meta)
        self.assertEqual(result[1].project, user_sheet_today.project)

    def test_project_service_sheets_returns_correct_ranking(self):
        """ Test timing of sheets returns correctly (x2) of x3 sheets
        (past, today. future) based on the overlap of time and ranking"""

        projectServiceIns = services
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'owner': self.user, 'url': 'test'}

        past_date = datetime.date.today() - datetime.timedelta(days=6)
        future_date = datetime.date.today() + datetime.timedelta(days=6)

        user_project = Project.objects.create(**project_data)

        user_sheet_past = Sheet.objects.create(project=user_project, owner=self.user, meta='past', ranking=999)
        user_sheet_today = Sheet.objects.create(project=user_project, owner=self.user, meta='today', ranking=10)
        user_sheet_future = Sheet.objects.create(project=user_project, owner=self.user, meta='future', ranking=100)

        TimeSync.objects.create(sheet=user_sheet_past, owner=self.user, durationVal=10, durationType='DY', date=past_date, meta=user_sheet_past.meta)
        TimeSync.objects.create(sheet=user_sheet_today, owner=self.user, durationVal=10, durationType='DY', meta=user_sheet_today.meta)
        TimeSync.objects.create(sheet=user_sheet_future, owner=self.user, durationVal=10, durationType='DY', date=future_date, meta=user_sheet_future.meta)

        result = projectServiceIns.collect_sheets_by_rank(user_project)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[1].id, user_sheet_past.id)
        self.assertEqual(result[1].meta, user_sheet_past.meta)
        self.assertEqual(result[1].project, user_sheet_past.project)
        self.assertEqual(result[0].id, user_sheet_today.id)
        self.assertEqual(result[0].meta, user_sheet_today.meta)
        self.assertEqual(result[0].project, user_sheet_today.project)

    def test_project_service_sheets_returns_equal_ranking_by_date(self):
        """ Test timing of sheets returns correctly order of sheets
            that have the same ranking but different creation dates """

        project_service_ins = services
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'owner': self.user, 'url': 'test'}

        past_date = datetime.datetime.now() - datetime.timedelta(days=6)

        user_project = Project.objects.create(**project_data)

        user_sheet_01 = Sheet.objects.create(project=user_project, owner=self.user, meta='01', ranking=900, createdAt=past_date)
        user_sheet_02 = Sheet.objects.create(project=user_project, owner=self.user, meta='02', ranking=900)

        result = project_service_ins.collect_sheets_by_rank(user_project)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, user_sheet_01.id)
        self.assertEqual(result[1].id, user_sheet_02.id)

    # // todo: Test for active/inactive projects

    def test_get_project_style_by_url(self):
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'url': 'fancy-url'}
        response = self.client.post('/api/project/', project_data, format='json')

        self.assertEqual(response.status_code, 200)

        response2 = self.client.get('/api/project/style/fancy-url.css')
        self.assertEqual(response2.status_code, 200)

        # test wrong url
        response2 = self.client.get('/api/project/style/fancy-url-missing.css')
        self.assertEqual(response2.status_code, 404)

    def test_get_project_style_should_refuse_base_url(self):
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'url': 'fancy-url'}
        response = self.client.post('/api/project/', project_data, format='json')

        self.assertEqual(response.status_code, 200)

        response2 = self.client.get('/api/project/style/base.css')
        self.assertEqual(response2.status_code, 404)

    def test_get_project_style_by_sheet_url(self):
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'url': 'fancy-no-url'}
        response_project = self.client.post('/api/project/', project_data, format='json')
        self.assertEqual(response_project.status_code, 200)

        response_data = json.loads(response_project.content)['data']
        sheet_data = {'name': 'testProject', 'owner': response_data['owner'], 'project': response_data['id'], 'url': 'fancy-sheet-url'}
        response_sheet = self.client.post('/api/sheet/', sheet_data, format='json')
        self.assertEqual(response_sheet.status_code, 200)

        response2 = self.client.get('/api/project/style/fancy-sheet-url.css')
        self.assertEqual(response2.status_code, 200)