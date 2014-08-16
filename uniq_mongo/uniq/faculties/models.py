from mongoengine import *
from schools.models import School
from uniq.genericmodels import *

class Faculty(GenericDocument):
	slug = StringField(unique_with='schoolId')
	schoolId = ObjectIdField()
	numPrograms = StringField()
	streams = ListField(EmbeddedDocumentField(Stream))
	importantDates = ListField(EmbeddedDocumentField(ImportantDate))
	applicationProcess = StringField()