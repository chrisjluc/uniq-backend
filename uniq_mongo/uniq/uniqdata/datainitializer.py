from models import SchoolModel, FacultyModel, ProgramModel
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
		for school_key, school_val in self.mapping.iteritems():
			school = SchoolModel(school_key, school_val, self.base_path)
			school.create_document()
			school_id = school.get_object_id()

			for faculty_key, faculty_val in school.mapping.iteritems():
				faculty = FacultyModel(faculty_key, faculty_val,
					 school.base_path, school_id)
				faculty.create_document()
				faculty_id = faculty.get_object_id()

				for program_key in faculty.mapping:
					program = ProgramModel(program_key, None,
						 faculty.base_path, school_id, faculty_id)
					program.create_document()
