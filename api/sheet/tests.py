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

    def test_sheet_create(self):
        project_data = {'name': 'testProject', 'meta': 'meta items here', 'url': 'test'}
        response_project = self.client.post('/api/project/', project_data, format='json')
        response_project_data = json.loads(response_project.content)['data']
        sheet_data = {
            'name': 'testSheet',
            'meta': 'meta items here',
            'owner': self.user,
            'project': Project.objects.get(id=response_project_data['id'])
        }
        user_sheet = Sheet.objects.create(**sheet_data)

        # // ensure 2 sheets exist
        self.assertEqual(Sheet.objects.all().count(), 2)





