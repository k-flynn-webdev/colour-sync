from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.test import TestCase
import json

from project.models import Project
from sheet.models import Sheet

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
        project_data = {'name': 'testProject', 'meta': 'meta items here'}
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
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'owner': self.user}
        project_data_other = {'name': 'testProject', 'meta': 'meta items here', 'owner': self.user_other}

        user_project = Project.objects.create(**project_data)
        user_other_project = Project.objects.create(**project_data_other)

        # // make sure 2 projects exist
        self.assertEqual(Project.objects.all().count(), 2)

        response = self.client.get(f'/api/project/{user_project.id}/', format='json')
        self.assertEqual(response.status_code, 200)

        response_other = self.client.get(f'/api/project/{user_other_project.id}/', format='json')
        self.assertEqual(response_other.status_code, 404)
