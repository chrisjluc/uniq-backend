from .models import *
from schools.models import *

from uniq.testing.testcases import MongoTestCase
from django.conf import settings
from rest_framework import status

class FacultyTests(MongoTestCase):

	sId = None
	fId = None

	def setUp(self):
		s = School(slug='s', metaData__yearValid=settings.CURRENT_YEAR)
		s.save()
		f = Faculty(slug='f', schoolId=s.id, metaData__yearValid=settings.CURRENT_YEAR)
		f.save()
		self.sId = s.id
		self.fId = f.id

	def tearDown(self):
		pass

	def test_get_list(self):
		response = self.client.get('/faculties/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_list_school_id(self):
		response = self.client.get('/schools/%s/faculties/' % self.sId, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_list_school_slug(self):
		response = self.client.get('/schools/s/faculties/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_detail_school_slug_faculty_slug(self):
		response = self.client.get('/schools/s/faculties/f/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_detail_faculty_id(self):
		response = self.client.get('/faculties/%s/' % self.fId, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_list_school_id_invalid(self):
		response = self.client.get('/schools/invalidid111/faculties/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_get_list_school_slug_invalid(self):
		response = self.client.get('/schools/invalidslug/faculties/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_get_detail_school_slug_faculty_slug_invalid(self):
		response = self.client.get('/schools/s/faculties/fsdfg/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_get_detail_faculty_id_invalid(self):
		response = self.client.get('/faculties/invalidId/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)