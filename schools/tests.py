from .models import *

from uniq.testing.testcases import MongoTestCase
from rest_framework import status
from django.conf import settings

class SchoolTests(MongoTestCase):

	sId = None

	def setUp(self):
		s = School(slug="s", metaData__yearValid=settings.CURRENT_YEAR)
		s.save()
		self.sId = s.id

	def tearDown(self):
		pass

	def test_get_listList(self):
		response = self.client.get('/schools/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_detail_slug(self):
		response = self.client.get('/schools/s/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_detail_id(self):
		response = self.client.get('/schools/%s/' % self.sId, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_detail_invalid_slug(self):
		response = self.client.get('/schools/asdf/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_get_detail_invalid_id(self):
		response = self.client.get('/schools/invalidid1/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)