from models import SchoolModel, FacultyModel, ProgramModel
from datainterceptors import *
from schools.models import School
from faculties.models import Faculty
from programs.models import Program
import json
import os.path
import logging

class DataInitializer(object):

	mapping_path = "mapping.json"

	def __init__(self, base_path = "./uniqdata/rawdata/"):
		print self.__class__.__name__
		self.Log = logging.getLogger(self.__class__.__name__)
		self.base_path = base_path
		data_path = base_path + self.mapping_path

		if os.path.isfile(data_path):
			with open(data_path) as data_file:
				self.mapping = json.load(data_file)
			self.is_valid = True
		else:
			self.is_valid = False

	def run(self):
		if self.is_valid is False:
			self.Log.warning("Path to %s is not a valid file path" % self.base_path)
			return

		s_interceptor = GenericInterceptor()
		f_interceptor = FacultyInterceptor()
		p_interceptor = ProgramInterceptor()

		for school_key, school_val in self.mapping.iteritems():
			school = SchoolModel(school_key, school_val, self.base_path, s_interceptor)
			if school.is_valid is False:
				self.Log.warning("Path to %s is not a valid file path" % school.data_path)
				continue
			school.create_document()
			school_id = school.object_id

			for faculty_key, faculty_val in school.mapping.iteritems():
				faculty = FacultyModel(faculty_key, faculty_val,
					 school.base_path, f_interceptor, school_id)
				if faculty.is_valid is False:
					self.Log.warning("Path to %s is not a valid file path" % faculty.data_path)
					continue
				faculty.create_document()
				faculty_id = faculty.object_id

				for program_key in faculty.mapping:
					program = ProgramModel(program_key, None,
						 faculty.base_path, p_interceptor, school_id, faculty_id)
					if program.is_valid is False:
						self.Log.warning("Path to %s is not a valid file path" % program.data_path)
						continue
					program.create_document()
