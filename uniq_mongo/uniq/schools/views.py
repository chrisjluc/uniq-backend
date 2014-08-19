from .models import School
from .serializers import SchoolSerializer
from uniqdata.finders import HistoricalFieldFinder

from rest_framework import generics, mixins, status
from rest_framework.response import Response
from django.conf import settings
from django.http import Http404
from bson.objectid import ObjectId
import datetime
import logging

class SchoolList(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
    
	serializer_class = SchoolSerializer

	def get_queryset(self):
		return School.objects

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

class SchoolDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					generics.GenericAPIView):
	
	serializer_class = SchoolSerializer
	
	def get_object(self):
		
		school_finder = SchoolFinder()

		if 'slug' in self.kwargs.keys():
			slug = self.kwargs['slug']
			try:
				return school_finder.get(slug=slug)
			except School.DoesNotExist:
				raise Http404
				
		if 'id' in self.kwargs.keys():
			id = self.kwargs['id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				return school_finder.get(id=id)
			except School.DoesNotExist:
				raise Http404

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

class SchoolFinder(object):

	def __init__(self):
		self.Log = logging.getLogger(self.__class__.__name__)
		if id:
			self.id = id
			return
		elif slug:
			self.slug = slug
			return
		self.Log.error("Got initialized without id or slug")

	def get(self, slug = None, id = None):
		#Keys
		name = 'name'
		short_name = 'shortName'
		about = 'about'
		app_process = 'applicationProcess'
		u_pop = 'undergradPopulation'
		g_pop = 'gradPopulation'
		avg_adm = 'avgAdm'
		date_est = 'dateEstablished'
		num_fac = 'numFaculties'
		num_pro = 'numPrograms'
		contacts = 'contacts'
		images = 'images'
		rankings = 'rankings'
		location = 'location'

		self.school = None
		self.hist = None

		if id:
			self.school = School.objects.get(id=id)
		elif slug:
			self.school = School.objects(slug=slug).first()

		self.hist = HistoricalFieldFinder(School.objects(slug=self.school.slug, metaData__yearValid__lt=settings.CURRENT_YEAR))

		self.apply_hist_value(name)
		self.apply_hist_value(short_name)
		self.apply_hist_value(about)
		self.apply_hist_value_with_year(app_process)
		self.apply_hist_value_with_year(u_pop)
		self.apply_hist_value_with_year(g_pop)
		self.apply_hist_value_with_year(avg_adm)
		self.apply_hist_value(date_est)
		self.apply_hist_value_with_year(num_fac)
		self.apply_hist_value_with_year(num_pro)
		self.apply_hist_value(contacts)
		self.apply_hist_value(images)
		self.apply_hist_value(rankings)
		self.apply_hist_value(location)

		return self.school

	def apply_hist_value_with_year(self, key):
		if not self.school[key]:
			val = self.hist.find_value(key, True)
			if val:
				self.school[key] = val

	def apply_hist_value(self, key):
		if not self.school[key]:
			print key
			val = self.hist.find_value(key, False)
			if val:
				self.school[key] = val


