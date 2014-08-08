from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .models import Faculty
from schools.models import School
from .serializers import FacultySerializer
from django.http import Http404
import datetime
from django.core.exceptions import ValidationError
from bson.objectid import ObjectId
import logging

class FacultyList(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
    
	serializer_class = FacultySerializer
	Log = None

	def __init__(self):
		Log = logging.getLogger(self.__class__.__name__)

	def get_queryset(self):
		keys = self.kwargs.keys()
		if 'school_slug' in keys:
			slug = self.kwargs['school_slug']
			try:
				school = School.objects.get(slug=slug)
				return Faculty.objects(schoolId=school.id)
			except School.DoesNotExist:
				raise Http404

		elif 'school_id' in keys:
			id = self.kwargs['school_id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				school = School.objects.get(id=id)
			except School.DoesNotExist:
				raise Http404

		return Faculty.objects

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class FacultyDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					generics.GenericAPIView):
	
	serializer_class = FacultySerializer
	Log = None

	def __init__(self):
		Log = logging.getLogger(self.__class__.__name__)

	def get_object(self):
		keys = self.kwargs.keys()
		if 'school_slug' in keys and 'slug' in keys:
			school_slug = self.kwargs['school_slug']
			slug = self.kwargs['slug']
			try:
				school = School.objects.get(slug=school_slug)
				return Faculty.objects.get(slug=slug, schoolId=school.id)
			except Faculty.DoesNotExist:
				raise Http404

		elif 'id' in self.kwargs.keys():
			id = self.kwargs['id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				return Faculty.objects.get(id=id)
			except Faculty.DoesNotExist:
				raise Http404

		Log.debug("Request doesn't have any parameters, but made it as a valid request")

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)