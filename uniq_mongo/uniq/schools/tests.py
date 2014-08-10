from rest_framework import status
from uniq.testing.testcases import MongoTestCase
from .models import *

class SchoolTests(MongoTestCase):

	def setUp(self):
		s = School(slug="s")
		s.save()

	def tearDown(self):
		pass

	def test_get_listList(self):
		response = self.client.get('/schools/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_detail_slug(self):
		response = self.client.get('/schools/s/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_detail_id(self):
		s = School(slug="f")
		s.save()
		response = self.client.get('/schools/%s/' % s.id, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_detail_invalid_slug(self):
		response = self.client.get('/schools/asdf/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_get_detail_invalid_id(self):
		response = self.client.get('/schools/invalidid1/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)