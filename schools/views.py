from django.shortcuts import render
from schools.models import School,Location,SchoolImage
from schools.serializers import (PostSchoolSerializer,GetSchoolSerializer,
	GetSchoolSuperUserSerializer,PostLocationSerializer,
	PostSchoolImageSerializer)
from rest_framework import generics,permissions
import datetime

class SchoolList(generics.ListCreateAPIView):
	queryset = School.objects.filter(toDelete=False)
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET' and user.is_superuser:
			return GetSchoolSuperUserSerializer
		elif self.request.method == 'GET':
			return GetSchoolSerializer
		return PostSchoolSerializer

class SchoolUpdate(generics.ListAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	serializer_class = GetSchoolSerializer

	def get_queryset(self):
		timeLastModified = int(self.kwargs['timeLastModified'])
		return School.objects.exclude(
			modified__gte=datetime.datetime.now()
		).filter(
			modified__gte=datetime.datetime.fromtimestamp(timeLastModified)
		)

class SchoolDetail(generics.RetrieveUpdateAPIView):
	queryset = School.objects.filter(toDelete=False)
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET' and user.is_superuser:
			return GetSchoolSuperUserSerializer
		elif self.request.method == 'GET':
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
		

