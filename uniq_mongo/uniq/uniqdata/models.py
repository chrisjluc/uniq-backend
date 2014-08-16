from schools.models import School
from faculties.models import Faculty
from programs.models import Program

from datainterceptors import *

from bson.objectid import ObjectId

import logging
import json

class Model(object):
		def __init__(self, slug, mapping):
			self.mapping = mapping
						
			with open(self.data_path) as data_file:
				self.data = json.load(data_file)

class SchoolModel(Model):

		def __init__(self, slug, mapping, base_path):
			self.base_path = base_path + slug + "/"
			self.data_path = self.base_path + slug + ".json"
			super(SchoolModel, self).__init__(slug, mapping)

		def create_document(self):
			interceptor = GenericInterceptor(self.data)
			school = School(**interceptor.data)
			school.save()

		def get_object_id(self):
			return self.document.id;

class FacultyModel(Model):

		def __init__(self, slug, mapping, base_path, school_id):

			self.base_path = base_path + slug + "/"
			self.data_path = self.base_path + slug + ".json"
			self.school_id = school_id
			super(FacultyModel, self).__init__(slug, mapping)
		
		def create_document(self):
			interceptor = FacultyInterceptor(self.data, self.school_id)
			faculty = Faculty(**interceptor.data)
			faculty.save()

		def get_object_id(self):
			return self.document.id;

class ProgramModel(Model):

		def __init__(self, slug, mapping, base_path, school_id, faculty_id):
			self.data_path = base_path + slug + ".json"
			self.school_id = school_id
			self.faculty_id = faculty_id
			super(ProgramModel, self).__init__(slug, mapping)

		def create_document(self):
			interceptor = ProgramInterceptor(self.data, self.school_id, self.faculty_id)
			program = Program(**interceptor.data)
			program.save()