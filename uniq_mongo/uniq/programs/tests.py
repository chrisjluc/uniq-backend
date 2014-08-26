from rest_framework import status
from uniq.testing.testcases import MongoTestCase
from .models import *
from faculties.models import *
from schools.models import *
from django.conf import settings

class ProgramTests(MongoTestCase):

	sId = None
	fId = None
	pId = None

	def setUp(self):
		s = School(slug='s', metaData__yearValid=settings.CURRENT_YEAR)
		s.save()
		f = Faculty(slug='f',schoolId=s.id, metaData__yearValid=settings.CURRENT_YEAR)
		f.save()
		p = Program(slug='p',schoolId=s.id, facultyId=f.id, metaData__yearValid=settings.CURRENT_YEAR)
		p.save()
		self.sId = s.id
		self.fId = f.id
		self.pId = p.id

	def tearDown(self):
		pass

	def test_get_list(self):
		response = self.client.get('/programs/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_list_faculty_id(self):
		response = self.client.get('/faculties/%s/programs/' % self.fId, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_list_school_slug_faculty_slug(self):
		response = self.client.get('/schools/s/faculties/f/programs/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_detail_school_slug_faculty_slug_program_slug(self):
		response = self.client.get('/schools/s/faculties/f/programs/p/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_detail_program_id(self):
		response = self.client.get('/programs/%s/' % self.pId, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_list_faculty_id_invalid(self):
		response = self.client.get('/faculties/invalidid1/programs/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_get_list_school_slug_faculty_slug_invalid(self):
		response = self.client.get('/schools/invalidslug/faculties/invalidslug/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_get_detail_school_slug_faculty_slug_program_slug_invalid(self):
		response = self.client.get('/schools/s/faculties/f/program/invalidslug/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_get_detail_program_id_invalid(self):
		response = self.client.get('/programs/invalidId/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)