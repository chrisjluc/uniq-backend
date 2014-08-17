from schools.models import School
from faculties.models import Faculty
from programs.models import Program
from uniq.genericmodels import GenericDocument

import time
from time import mktime
from datetime import datetime

class GenericInterceptor(object):
	
	def intercept(self, data):
			# Meta data 
			data['metaData']['dateModified'] = datetime.utcnow()
			data['metaData']['dateCreated'] = datetime.utcnow()
			struct = time.strptime(data['dateEstablished'] , "%d-%m-%Y")
			data['dateEstablished'] = datetime.fromtimestamp(mktime(struct))

			# Contact
			for contact in data['contacts']:
				for key, val in contact.iteritems():
					if val == '':
						contact[key] = None
			self.data = data
		
class FacultyInterceptor(GenericInterceptor):

		def intercept(self, data, school_id):
			data['schoolId'] = school_id
			super(FacultyInterceptor, self).intercept(data)

class ProgramInterceptor(GenericInterceptor):
	
		def intercept(self, data, school_id, faculty_id):
			data['schoolId'] = school_id
			data['facultyId'] = faculty_id
			super(ProgramInterceptor, self).intercept(data)

