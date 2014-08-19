from django.conf import settings
from schools.models import School
from faculties.models import Faculty

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
					return obj[key].strip() + " ({0})".format(year)
				return obj[key].strip()
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
		if isinstance(obj) is Faculty:
			self.type = 'faculty'
		elif isinstance(obj) is Program:
			self.type = 'program'
			faculty_finder = FacultyFinder()
			self.faculty = faculty_finder.get(id=obj.facultyId)
		else:
			#TODO: log error, doesn't accept other types
			return
		
		school_finder = SchoolFinder()
		self.school = school_finder.get(id=obj.schoolId)
			
		
	def find_value(self, key):
		if self.type is 'faculty':
			if self.school and self.school[key]:
				return self.school[key].strip()
		elif self.type is 'program':
			if self.faculty and self.faculty[key]:
				return self.faculty[key].strip()
			if self.school and self.school[key]:
				return self.school[key].strip()
		return None
		
class HistoricalHierarchicalFieldFinder(object):
	'''
		Runs historical field finder, if it doesn't return a value
		then run hierarchical field finder
	'''
	
	def __init__(self, obj, objects):
		historical_finder = HistoricalFieldFinder(objects)
		hierarchical_finder = HierarchicalFieldFinder(obj)
	
	def find_value(self, key, append_year = False):
		val = historical_finder.find_value(key, append_year)
		if val:
			return val
		val = hierarchical_finder.find_value(key)
		if val:
			return val
		return None
