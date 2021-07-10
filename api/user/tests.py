from django.contrib.auth import get_user_model
from .context_processors import template_vars
from rest_framework.test import APIClient
from django.test import TestCase
import json

User = get_user_model()

# store the password to login later
password = 'mypassword'


# Create your tests here.
class BasicTests(TestCase):

    def login(self):
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.client = APIClient()
        self.client.login(email=my_admin.email, password=password)

    def setUp(self):
        self.login()

    def test_template_vars(self):
        vars = template_vars(None)
        self.assertTrue(vars['APP_NAME_SHORT'])
        self.assertTrue(vars['APP_NAME_FULL'])
        self.assertTrue(vars['META_AUTHOR'])
        self.assertTrue(vars['META_DESCRIPTION'])

    def test_whoami_with_user(self):
        response = self.client.get('/api/whoami/')
        self.assertEqual(response.status_code, 200)
        self.assertEquals(json.loads(response.content)['detail'], 'User found.')
        self.assertContains(response, 'id')
        self.assertContains(response, 'meta')
        self.assertContains(response, 'email')
        self.assertContains(response, 'last_login')
        self.assertContains(response, 'date_joined')

    def test_whoami_with_no_user(self):
        self.client.logout()
        response = self.client.get('/api/whoami/')
        self.assertEqual(response.status_code, 200)
        self.assertEquals(json.loads(response.content)['detail'], 'No user logged in.')
        self.assertFalse(json.loads(response.content)['data'])
