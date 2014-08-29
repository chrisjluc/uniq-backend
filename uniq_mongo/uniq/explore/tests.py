from uniq.testing.testcases import MongoTestCase
from programs.models import *
from faculties.models import *
from schools.models import *

from rest_framework import status
from django.conf import settings

class ExploreTests(MongoTestCase):

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

	def test_schools(self):
		response = self.client.get('/explore/schools/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_faculties(self):
		response = self.client.get('/explore/faculties/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_faculties_schoolId(self):
		response = self.client.get('/explore/faculties/%s/' % self.sId, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_faculties_id_invalid(self):
		response = self.client.get('/explore/faculties/%s/' % self.pId, format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_programs(self):
		response = self.client.get('/explore/programs/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_programs_facultyId(self):
		response = self.client.get('/explore/programs/%s/' % self.fId, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_programs_id_invalid(self):
		response = self.client.get('/explore/programs/%s/' % self.pId, format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
