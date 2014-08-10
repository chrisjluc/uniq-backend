from rest_framework import generics, mixins, status
from rest_framework.response import Response
from models import Program
from faculties.models import Faculty
from schools.models import School
from faculties.serializers import FacultySerializer
from serializers import ProgramSerializer
from django.http import Http404
import datetime
from bson.objectid import ObjectId
import logging

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
				school = School.objects.get(slug=school_slug)
				faculty = Faculty.objects.get(schoolId=school.id, slug=faculty_slug)
				return Program.objects(schoolId=school.id,facultyId=faculty.id)
			except School.DoesNotExist:
				raise Http404

		elif 'faculty_id' in keys:
			id = self.kwargs['faculty_id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				return Program.objects.get(facultyId=id)
			except School.DoesNotExist:
				raise Http404

		return Program.objects

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class ProgramDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					generics.GenericAPIView):
	
	serializer_class = FacultySerializer
	Log = None

	def __init__(self):
		Log = logging.getLogger(self.__class__.__name__)

	def get_object(self):
		keys = self.kwargs.keys()

		if ('school_slug' in keys
		and 'faculty_slug' in keys
		and 'slug' in keys):
			school_slug = self.kwargs['school_slug']
			faculty_slug = self.kwargs['faculty_slug']
			slug = self.kwargs['slug']
			try:
				school = School.objects.get(slug=school_slug)
				faculty = Faculty.objects.get(schoolId=school.id, slug=faculty_slug)
				return Program.objects.get(schoolId=school.id, facultyId=faculty.id, slug=slug)
			except Program.DoesNotExist:
				raise Http404

		if 'id' in self.kwargs.keys():
			id = self.kwargs['id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				return Program.objects.get(id=id)
			except Program.DoesNotExist:
				raise Http404

		Log.debug("Request doesn't have any parameters, but made it as a valid request")
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)