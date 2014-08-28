from faculties.serializers import FacultySerializer
from serializers import ProgramSerializer
from uniqdata.documentfinders import *

from rest_framework import generics, mixins, status
from rest_framework.response import Response
from django.http import Http404
import datetime
from bson.objectid import ObjectId
import logging

school_finder = SchoolFinder()
faculty_finder = FacultyFinder()
program_finder = ProgramFinder()

class ProgramList(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
    
	serializer_class = ProgramSerializer

	def get_queryset(self):
		keys = self.kwargs.keys()
		if 'school_slug' in keys and 'faculty_slug' in keys:
			school_slug = self.kwargs['school_slug']
			faculty_slug = self.kwargs['faculty_slug']
			try:
				school = school_finder.get(slug=school_slug)
				faculty = faculty_finder.get(school_id=school.id, slug=faculty_slug)
				return program_finder.all(faculty_id=faculty.id)
			except:
				raise Http404

		elif 'faculty_id' in keys:
			id = self.kwargs['faculty_id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				return program_finder.all(faculty_id=id)
			except:
				raise Http404

		return program_finder.all()

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class ProgramDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					generics.GenericAPIView):
	
	serializer_class = ProgramSerializer

	def __init__(self):
		self.Log = logging.getLogger(self.__class__.__name__)

	def get_object(self):
		keys = self.kwargs.keys()

		if ('school_slug' in keys
		and 'faculty_slug' in keys
		and 'slug' in keys):
			school_slug = self.kwargs['school_slug']
			faculty_slug = self.kwargs['faculty_slug']
			slug = self.kwargs['slug']
			try:
				school = school_finder.get(slug=school_slug)
				faculty = faculty_finder.get(school_id=school.id, slug=faculty_slug)
				return program_finder.get(slug=slug, faculty_id=faculty.id)
			except:
				raise Http404

		if 'id' in self.kwargs.keys():
			id = self.kwargs['id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				return program_finder.get(id=id)
			except:
				raise Http404

		self.Log.debug("Request doesn't have any parameters, but made it as a valid request")
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)