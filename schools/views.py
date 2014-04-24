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
		if self.request.method == 'POST':
			return PostSchoolSerializer
		return GetSchoolSerializer
	

class SchoolDetail(generics.RetrieveUpdateAPIView):
	queryset = School.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'POST':
			return PostSchoolSerializer
		return GetSchoolSerializer

class Location(generics.CreateAPIView):
	queryset = Location.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'POST':
			return PostLocationSerializer
		return GetLocationSerializer

class SchoolImage(generics.CreateAPIView):
	queryset = SchoolImage.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'POST':
			return PostSchoolImageSerializer
		return GetSchoolImageSerializer

