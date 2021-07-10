from django.test import RequestFactory, TestCase
from .views import get_csrf
import json


# Create your tests here.
class BasicTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_csrf_on_request(self):
        request = self.factory.get('')
        response = get_csrf(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(json.loads(response.content)['detail']) > 5)
        self.assertEquals(json.loads(response.content)['detail'], 'CSRF cookie set')
        self.assertTrue(len(json.loads(response.content)['data']) > 25)
