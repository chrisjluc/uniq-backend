from mongoengine import *
from schools.models import School
from uniq.genericmodels import *

class Faculty(GenericDocument):
	numPrograms = IntField()
	schoolId = ObjectIdField()
	streams = ListField(EmbeddedDocumentField(Stream))
	importantDates = ListField(EmbeddedDocumentField(ImportantDate))
	applicationProcess = StringField()