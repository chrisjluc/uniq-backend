from django.shortcuts import render
from schools.models import School,Location,SchoolImage,SchoolRanking
from schools.serializers import (PostSchoolSerializer,GetSchoolSerializer,
	GetSchoolSuperUserSerializer,LocationSuperUserSerializer,GetLocationSerializer,
	SchoolImageSuperUserSerializer,GetSchoolImageSerializer,GetSchoolRankingSerializer,
	SchoolRankingSuperUserSerializer)
from rest_framework import generics,permissions
import datetime


class SchoolList(generics.ListCreateAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		schools = School.objects.filter(toDelete=False)
		return schools
	
	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET' and user.is_superuser:
			return GetSchoolSuperUserSerializer
		elif self.request.method == 'GET':
			return GetSchoolSerializer
		return PostSchoolSerializer

class SchoolUpdate(generics.ListAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
	def get_serializer_class(self):
		user = self.request.user
		if user.is_superuser:
			return GetSchoolSuperUserSerializer
		return GetSchoolSerializer


	def get_queryset(self):
		timeLastModified = int(self.kwargs['timeLastModified'])
		return School.objects.exclude(
			modified__gte=datetime.datetime.now()
		).filter(
			modified__gt=datetime.datetime.fromtimestamp(timeLastModified)
		)

class SchoolDetail(generics.RetrieveUpdateAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		schools = School.objects.filter(toDelete=False)
		for school in schools:
			school.images = [image for image in school.images.all() if image.toDelete == False]
		return schools
	
	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET' and user.is_superuser:
			return GetSchoolSuperUserSerializer
		elif self.request.method == 'GET':
			return GetSchoolSerializer
		return PostSchoolSerializer		

class Location(generics.CreateAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_serializer_class(self):
		user = self.request.user
		if user.is_superuser:
			return LocationSuperUserSerializer
		return GetLocationSerializer	

class SchoolImage(generics.CreateAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_serializer_class(self):
		user = self.request.user
		if user.is_superuser:
			return SchoolImageSuperUserSerializer
		return GetSchoolImageSerializer

class SchoolRanking(generics.CreateAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_serializer_class(self):
		user = self.request.user
		if user.is_superuser:
			return SchoolRankingSuperUserSerializer
		return GetSchoolRankingSerializer
		

