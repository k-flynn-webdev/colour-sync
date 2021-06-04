import json
from django.test import RequestFactory, TestCase
from django.contrib.auth import get_user_model
from .context_processors import template_vars

User = get_user_model()

# store the password to login later
password = 'mypassword'


# Create your tests here.
class BasicTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.client.login(username=my_admin.username, password=password)

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
        self.assertContains(response, 'last_login')
        self.assertContains(response, 'id')

    def test_whoami_with_no_user(self):
        self.client.logout()
        response = self.client.get('/api/whoami/')
        self.assertEqual(response.status_code, 200)
        self.assertEquals(json.loads(response.content)['detail'], 'No user logged in.')
        self.assertFalse(json.loads(response.content)['data'])
