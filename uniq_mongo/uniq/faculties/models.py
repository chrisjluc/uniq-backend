from mongoengine import *
from schools.models import School
from uniq.genericmodels import GenericDocument

class Faculty(GenericDocument):
	numPrograms = IntField()
	schoolId = ObjectIdField()