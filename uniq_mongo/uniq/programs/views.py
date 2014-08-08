from rest_framework import generics, mixins, status
from rest_framework.response import Response
from models import Program
from faculties.models import Faculty
from schools.models import School
from faculties.serializers import FacultySerializer
from serializers import ProgramSerializer
from django.http import Http404
import datetime
from django.core.exceptions import ValidationError
from bson.objectid import ObjectId

class ProgramList(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
    
	serializer_class = ProgramSerializer

	def get_queryset(self):
		faculty = None
		'''if 'slug' in self.kwargs.keys():
			slug = self.kwargs['slug']
			try:
				school = School.objects.get(slug=slug)
			except School.DoesNotExist:
				raise Http404'''

		if 'id' in self.kwargs.keys():
			id = self.kwargs['id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				faculty = Faculty.objects.get(id=id)
			except Faculty.DoesNotExist:
				raise Http404

		if faculty is None:
			return Program.objects
		return Program.objects(facultyId=faculty.id)

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class ProgramDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					generics.GenericAPIView):
	
	serializer_class = FacultySerializer
	
	def get_object(self):
		if 'slug' in self.kwargs.keys():
			slug = self.kwargs['slug']
			try:
				return Program.objects.get(slug=slug)
			except Program.DoesNotExist:
				raise Http404

		if 'id' in self.kwargs.keys():
			id = self.kwargs['id']
			try:
				return Program.objects.get(id=id)
			except Program.DoesNotExist:
				raise Http404

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)