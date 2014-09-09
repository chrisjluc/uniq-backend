from uniq.testing.testcases import MongoTestCase
from .models import *

from rest_framework import status
from django.conf import settings
import json

class FeaturedTests(MongoTestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_featured_empty(self):
		response = self.client.get('/featured/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 0)

	def test_featured_1_item(self):
		Featured().save()
		response = self.client.get('/featured/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_featured_multiple_item(self):
		Featured().save()
		Featured().save()
		Featured().save()

		response = self.client.get('/featured/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 3)


	def test_featured_order_priority(self):
		Featured(priority=2).save()
		Featured(priority=1).save()
		response = self.client.get('/featured/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data[0]['priority'], 1)
		self.assertEqual(response.data[1]['priority'], 2)

	def test_featured_order_datetime(self):
		Featured(nameTitle='first').save()
		Featured(nameTitle='second').save()
		response = self.client.get('/featured/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data[0]['nameTitle'], 'first')
		self.assertEqual(response.data[1]['nameTitle'], 'second')

	def test_featured_constrained_max_items(self):
		for i in xrange(0,settings.MAX_FEATURED+3):
			Featured().save()
		response = self.client.get('/featured/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), settings.MAX_FEATURED)

	def test_featured_create_new_item(self):
		response = self.client.post('/featured/', 
			{
			    "featuredTitle": "", 
			    "nameTitle": "", 
			    "type": "", 
			    "priority": 0, 
			    "dateCreated": None, 
			    "dateExpired": None, 
			    "image_link": "https://wiki.python.org/"
			} ,format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		response = self.client.get('/featured/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)
