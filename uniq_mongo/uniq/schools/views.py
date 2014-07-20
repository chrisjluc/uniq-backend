from rest_framework import generics, mixins, status
from rest_framework.response import Response

from .models import School
from .serializers import SchoolSerializer

from django.http import Http404

import datetime


class SchoolList(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
    
	serializer_class = SchoolSerializer

	def get_queryset(self):
		return School.objects

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = request.DATA
		if data['slug'] is None or not data['slug']:
			data['slug'] = data['name'].lower().replace(" ", "")
		return self.create(request, *args, **kwargs)

class SchoolDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	
	serializer_class = SchoolSerializer
	
	def get_object(self):
		slug = self.kwargs['slug']
		print slug
		try:
			return School.objects.get(slug=slug)
		except School.DoesNotExist:
			raise Http404

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)