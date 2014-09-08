from schools.models import School
from faculties.models import Faculty
from programs.models import Program

from uniqdata.documentfinders import *
from .serializers import *

from rest_framework import generics
from rest_framework.response import Response

from django.conf import settings
from django.http import *
from django.core.cache import caches

from bson.objectid import ObjectId
import datetime
import logging

school_cache=caches['school_explore']
faculty_cache=caches['faculty_explore']
program_cache=caches['program_explore']

class SchoolExplore(generics.ListAPIView):
    
	serializer_class = ExploreSerializer

	def get_queryset(self):
		school = school_cache.get('school_explore')
		if not school:
			school = SchoolFinder().all()
			school_cache.set('school_explore', school)
		return school

class FacultyExplore(generics.ListAPIView):

	serializer_class = ExploreSerializer

	def get_queryset(self):
		ret = None
		if 'school_id' in self.kwargs.keys():
			id = self.kwargs['school_id']
			if ObjectId.is_valid(id) is False:
				raise Http400
			try:
				ret = faculty_cache.get('faculty_explore'+id)
				if not ret:
					ret = FacultyFinder().all(school_id=id)
					faculty_cache.set('faculty_explore'+id, ret)
			except:
				raise Http404
		else:
			ret = faculty_cache.get('faculty_explore')
			if not ret:
				ret = FacultyFinder().all()
				faculty_cache.set('faculty_explore', ret)

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
				raise Http400
			try:
				ret = program_cache.get('program_explore'+id)
				if not ret:
					ret = ProgramFinder().all(faculty_id=id)
					program_cache.set('program_explore'+id, ret)
			except:
				raise Http404
		else:
			ret = program_cache.get('program_explore')
			if not ret:
				ret = ProgramFinder().all()
				program_cache.set('program_explore', ret)

		if len(ret) is 0:
			raise Http404
			
		return ret

class ProgramExploreDetail(generics.RetrieveAPIView):
	
	serializer_class = ExploreSerializer

	def get_object(self):
		keys = self.kwargs.keys()

		if 'id' in keys:
			id = self.kwargs['id']
			ret = program_cache.get('program_explore_detail'+id)
			if not ret:
				try:
					ret = ProgramFinder().get(id=id)
				except Program.DoesNotExist:
					raise Http404
				program_cache.set('program_explore_detail'+id, ret)
			return ret

		raise Http400
