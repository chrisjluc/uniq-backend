
from schools.models import School
from faculties.models import Faculty
from programs.models import Program

from uniqdata.documentfinders import *
from .serializers import *

from rest_framework import generics
from rest_framework.response import Response
from django.conf import settings
from django.http import Http404
from bson.objectid import ObjectId

import datetime
import logging

class SchoolExplore(generics.ListAPIView):
    
	serializer_class = ExploreSerializer

	def get_queryset(self):
		return SchoolFinder().all()

class FacultyExplore(generics.ListAPIView):

	serializer_class = ExploreSerializer

	def get_queryset(self):
		ret = None
		if 'school_id' in self.kwargs.keys():
			id = self.kwargs['school_id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				ret = FacultyFinder().all(school_id=id)
			except:
				raise Http404
		else:
			ret = FacultyFinder().all()

		if len(ret) is 0:
			raise Http404

		return ret

class ProgramExplore(generics.ListAPIView):

	serializer_class = ExploreSerializer

	def get_queryset(self):
		ret = None
		if 'faculty_id' in self.kwargs.keys():
			id = self.kwargs['faculty_id']
			if ObjectId.is_valid(id) is False:
				raise Http404
			try:
				ret = ProgramFinder().all(faculty_id=id)
			except:
				raise Http404
		else:
			ret = ProgramFinder().all()

		if len(ret) is 0:
			raise Http404
			
		return ret