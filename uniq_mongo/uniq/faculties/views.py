from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .models import Faculty
from schools.models import School
from .serializers import FacultySerializer
from django.http import Http404
import datetime
from django.core.exceptions import ValidationError
from bson.objectid import ObjectId

class FacultyList(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
    
	serializer_class = FacultySerializer

	def get_queryset(self):
		school = None
		if 'slug' in self.kwargs.keys():
			slug = self.kwargs['slug']
			try:
				school = School.objects.get(slug=slug)
			except School.DoesNotExist:
				raise Http404

		if 'id' in self.kwargs.keys():
			id = self.kwargs['id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				school = School.objects.get(id=id)
			except School.DoesNotExist:
				raise Http404

		if school is None:
			return Faculty.objects
		return Faculty.objects(schoolId=school.id)

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class FacultyDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					generics.GenericAPIView):
	
	serializer_class = FacultySerializer
	
	def get_object(self):
		if 'slug' in self.kwargs.keys():
			slug = self.kwargs['slug']
			try:
				return Faculty.objects.get(slug=slug)
			except Faculty.DoesNotExist:
				raise Http404

		if 'id' in self.kwargs.keys():
			id = self.kwargs['id']
			try:
				return Faculty.objects.get(id=id)
			except Faculty.DoesNotExist:
				raise Http404

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)