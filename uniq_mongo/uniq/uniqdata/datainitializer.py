from models import SchoolModel, FacultyModel, ProgramModel
from datainterceptors import *
from schools.models import School
from faculties.models import Faculty
from programs.models import Program
import json

class DataInitializer(object):

	mapping_path = "mapping.json"

	def __init__(self, base_path = "./uniqdata/rawdata/"):
		self.base_path = base_path
		with open(base_path + self.mapping_path) as data_file:
			self.mapping = json.load(data_file)

	def run(self):
		s_interceptor = GenericInterceptor()
		f_interceptor = FacultyInterceptor()
		p_interceptor = ProgramInterceptor()

		for school_key, school_val in self.mapping.iteritems():
			school = SchoolModel(school_key, school_val, self.base_path, s_interceptor)
			school.create_document()
			school_id = school.object_id

			for faculty_key, faculty_val in school.mapping.iteritems():
				faculty = FacultyModel(faculty_key, faculty_val,
					 school.base_path, f_interceptor, school_id)
				faculty.create_document()
				faculty_id = faculty.object_id

				for program_key in faculty.mapping:
					program = ProgramModel(program_key, None,
						 faculty.base_path, p_interceptor, school_id, faculty_id)
					program.create_document()
