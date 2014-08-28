from django.conf import settings
from faculties.models import Faculty
from programs.models import Program

class HistoricalFieldFinder(object):
	'''
		Assume objects are given to it in newest to oldest
	'''

	def __init__(self, objects):
		self.objects = objects
	
	def find_value(self, key, append_year = False):
		for obj in self.objects:
			if obj['metaData']['yearValid'] >= settings.CURRENT_YEAR:
				continue
			if obj[key]:
				if append_year is True:
					year = str(obj['metaData']['yearValid'])
					return obj[key] + " ({0})".format(year)
				return obj[key]
		return None

class HierarchicalFieldFinder(object):
	'''
		Programs can look at first faculties, then schools for missing information
		Faculties can look at schools
		
		Assume it will be given the most up-to-date info
		through the faculty and/or school finders
	'''
	
	# object can be either faculty or program
	def __init__(self, obj):
		if isinstance(obj, Faculty):
			self.type = 'faculty'
		elif isinstance(obj, Program):
			self.type = 'program'
			from documentfinders import FacultyFinder
			self.faculty = FacultyFinder().get(id=obj.facultyId)
		else:
			#TODO: log error, doesn't accept other types
			return
		from documentfinders import SchoolFinder
		self.school = SchoolFinder().get(id=obj.schoolId)
			
		
	def find_value(self, key):
		if self.type is 'faculty':
			if self.school and key in self.school:
				return self.school[key]
		elif self.type is 'program':
			if self.faculty and key in self.faculty:
				return self.faculty[key]
			if self.school and key in self.school:
				return self.school[key]
		return None
		
class HistoricalHierarchicalFieldFinder(object):
	'''
		Runs historical field finder, if it doesn't return a value
		then run hierarchical field finder
	'''
	
	def __init__(self, obj, objects):
		self.historical_finder = HistoricalFieldFinder(objects)
		self.hierarchical_finder = HierarchicalFieldFinder(obj)
	
	def find_value(self, key, append_year = False):
		val = self.historical_finder.find_value(key, append_year)
		if val:
			return val
		val = self.hierarchical_finder.find_value(key)
		if val:
			return val
		return None




