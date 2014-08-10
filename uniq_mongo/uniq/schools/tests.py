from rest_framework import status
from rest_framework.test import APITestCase

class SchoolTests(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def schools_get(self):
        factory = APIRequestFactory()
        request = factory.get('/schools/')