from django.shortcuts import render
from faculties.models import Faculty,FacultyImage
from faculties.serializers import (PostFacultySerializer,GetFacultySerializer,
	GetFacultySuperUserSerializer, FacultyImageSuperUserSerializer,GetFacultyImageSerializer)
from rest_framework import generics,permissions
import datetime

class FacultiesInSchoolList(generics.ListAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		schoolId = int(self.kwargs['schoolId'])
		Faculties = Faculty.objects.filter(schoolId=schoolId)
		return Faculties
	
	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET' and user.is_superuser:
			return GetFacultySuperUserSerializer
		elif self.request.method == 'GET':
			return GetFacultySerializer


class FacultyList(generics.ListCreateAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		Faculties = Faculty.objects.filter(toDelete=False)
		return Faculties
	
	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET' and user.is_superuser:
			return GetFacultySuperUserSerializer
		elif self.request.method == 'GET':
			return GetFacultySerializer
		return PostFacultySerializer

class FacultyUpdate(generics.ListAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
	def get_serializer_class(self):
		user = self.request.user
		if user.is_superuser:
			return GetFacultySuperUserSerializer
		return GetFacultySerializer

	def get_queryset(self):
		timeLastModified = int(self.kwargs['timeLastModified'])
		return Faculty.objects.exclude(
			modified__gte=datetime.datetime.now()
		).filter(
			modified__gt=datetime.datetime.fromtimestamp(timeLastModified)
		)

class FacultyDetail(generics.RetrieveUpdateAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		Faculties = Faculty.objects.filter(toDelete=False)
		return Faculties
	
	def get_serializer_class(self):
		user = self.request.user
		if self.request.method == 'GET' and user.is_superuser:
			return GetFacultySuperUserSerializer
		elif self.request.method == 'GET':
			return GetFacultySerializer
		return PostFacultySerializer		

class FacultyImage(generics.CreateAPIView):

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_serializer_class(self):
		user = self.request.user
		if user.is_superuser:
			return FacultyImageSuperUserSerializer
		return GetFacultyImageSerializer
		

