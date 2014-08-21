from .models import School
from .serializers import SchoolSerializer
from uniqdata.documentfinders import SchoolFinder

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
		return SchoolFinder.all()

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

class SchoolDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					generics.GenericAPIView):
	
	serializer_class = SchoolSerializer
	
	def get_object(self):
		
		if 'slug' in self.kwargs.keys():
			slug = self.kwargs['slug']
			try:
				return SchoolFinder.get(slug=slug)
			except School.DoesNotExist:
				raise Http404
				
		if 'id' in self.kwargs.keys():
			id = self.kwargs['id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				return SchoolFinder.get(id=id)
			except School.DoesNotExist:
				raise Http404

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)