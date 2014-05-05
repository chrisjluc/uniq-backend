from django.shortcuts import render
from schools.models import School,Location,SchoolImage
from schools.serializers import (PostSchoolSerializer,GetSchoolSerializer,
	PostLocationSerializer,GetLocationSerializer,
	PostSchoolImageSerializer,GetSchoolImageSerializer)
from rest_framework import generics
from rest_framework import permissions

class SchoolList(generics.ListCreateAPIView):
	queryset = School.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET':
			return GetSchoolSerializer
		return PostSchoolSerializer
		
	

class SchoolDetail(generics.RetrieveUpdateAPIView):
	queryset = School.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET':
			return GetSchoolSerializer
		return PostSchoolSerializer
		

class Location(generics.CreateAPIView):
	queryset = Location.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET':
			return GetLocationSerializer
		return PostLocationSerializer
		

class SchoolImage(generics.CreateAPIView):
	queryset = SchoolImage.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET':
			return GetSchoolImageSerializer
		return PostSchoolImageSerializer
		

