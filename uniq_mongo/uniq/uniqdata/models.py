from schools.models import School
from faculties.models import Faculty
from programs.models import Program

from bson.objectid import ObjectId

import logging
import json

class Model(object):
		def __init__(self, slug, mapping, interceptor):
			self.mapping = mapping
			self.interceptor = interceptor
						
			with open(self.data_path) as data_file:
				self.data = json.load(data_file)

class SchoolModel(Model):

		def __init__(self, slug, mapping, base_path, interceptor):
			self.base_path = base_path + slug + "/"
			self.data_path = self.base_path + slug + ".json"
			super(SchoolModel, self).__init__(slug, mapping, interceptor)

		def create_document(self):
			self.interceptor.intercept(self.data)
			school = School(**self.interceptor.data)
			school.save()
			self.object_id = school.id

class FacultyModel(Model):

		def __init__(self, slug, mapping, base_path, interceptor, school_id):

			self.base_path = base_path + slug + "/"
			self.data_path = self.base_path + slug + ".json"
			self.school_id = school_id
			super(FacultyModel, self).__init__(slug, mapping, interceptor)
		
		def create_document(self):
			self.interceptor.intercept(self.data, self.school_id)
			faculty = Faculty(**self.interceptor.data)
			faculty.save()
			self.object_id = faculty.id

class ProgramModel(Model):

		def __init__(self, slug, mapping, base_path, interceptor, school_id, faculty_id):
			self.data_path = base_path + slug + ".json"
			self.school_id = school_id
			self.faculty_id = faculty_id
			super(ProgramModel, self).__init__(slug, mapping, interceptor)

		def create_document(self):
			self.interceptor.intercept(self.data, self.school_id, self.faculty_id)
			program = Program(**self.interceptor.data)
			program.save()