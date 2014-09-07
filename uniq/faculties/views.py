from .models import Faculty
from .serializers import FacultySerializer
from uniqdata.documentfinders import *

from rest_framework import generics, mixins, status
from rest_framework.response import Response

from django.http import Http404
from django.core.cache import caches

import datetime
from bson.objectid import ObjectId
import logging

cache = caches['faculty']
school_finder = SchoolFinder()
faculty_finder = FacultyFinder()

class FacultyList(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
    
	serializer_class = FacultySerializer

	def get_queryset(self):
		keys = self.kwargs.keys()
		if 'school_slug' in keys:
			slug = self.kwargs['school_slug']
			try:
				return faculty_finder.all(school_slug=slug)
			except:
				raise Http404

		elif 'school_id' in keys:
			id = self.kwargs['school_id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				return faculty_finder.all(school_id=id)
			except:
				raise Http404

		return faculty_finder.all()

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class FacultyDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					generics.GenericAPIView):
	
	serializer_class = FacultySerializer

	def __init__(self):
		self.Log = logging.getLogger(self.__class__.__name__)

	def get_object(self):
		keys = self.kwargs.keys()
		if 'school_slug' in keys and 'slug' in keys:
			school_slug = self.kwargs['school_slug']
			slug = self.kwargs['slug']
			try:
				school = school_finder.get(slug=school_slug)
				return faculty_finder.get(slug=slug, school_id=school.id)
			except:
				raise Http404

		elif 'id' in self.kwargs.keys():
			id = self.kwargs['id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				faculty = cache.get(id)
				if not faculty:
					faculty = faculty_finder.get(id=id)
					cache.set(id, faculty)
				return faculty
			except:
				raise Http404

		self.Log.debug("Request doesn't have any parameters, but made it as a valid request")

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)