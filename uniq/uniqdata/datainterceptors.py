from schools.models import School
from faculties.models import Faculty
from programs.models import Program
from uniq.genericmodels import *

import time
from time import mktime
from datetime import datetime

class GenericInterceptor(object):
	
	def intercept(self, data):
			# Meta data 
			data['metaData']['dateModified'] = datetime.utcnow()
			data['metaData']['dateCreated'] = datetime.utcnow()
			if data['dateEstablished']:
				struct = time.strptime(data['dateEstablished'] , "%d-%m-%Y")
				data['dateEstablished'] = datetime.fromtimestamp(mktime(struct))
			else:
				data['dateEstablished'] = None

			# Contact
			if data['contacts'] is not None:
				for contact in data['contacts']:
					for key, val in contact.iteritems():
						if val == '':
							contact[key] = None
			return data
		
class FacultyInterceptor(GenericInterceptor):

		def intercept(self, data, school_id):
			data['schoolId'] = school_id
			return super(FacultyInterceptor, self).intercept(data)

class ProgramInterceptor(GenericInterceptor):
	
		def intercept(self, data, school_id, faculty_id):
			data['schoolId'] = school_id
			data['facultyId'] = faculty_id
			return super(ProgramInterceptor, self).intercept(data)

		def related_intercept(self, _program, keys):
			if keys is None or len(keys) is 0:
				return
			ids = []
			_program.related = Related()
			_program.related.relatedIds = []
			for key in keys:
				slugs = key.split('_')
				school = School.objects(slug=slugs[0]).order_by("-metaData.yearValid").first()
				faculty = Faculty.objects(schoolId=school.id, slug=slugs[1]).order_by("-metaData.yearValid").first()
				program = Program.objects(facultyId=faculty.id, slug=slugs[2]).order_by("-metaData.yearValid").first()
				_program.related.relatedIds.append(str(program.id))
			_program.save()





