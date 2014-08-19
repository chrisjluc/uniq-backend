from mongoengine import *
from schools.models import School
from uniq.genericmodels import *

class Faculty(GenericDocument):
	slug = StringField(unique_with=['schoolId', 'metaData.yearValid'])
	schoolId = ObjectIdField()
	numPrograms = StringField()
	streams = ListField(EmbeddedDocumentField(Stream))
	importantDates = ListField(EmbeddedDocumentField(ImportantDate))
	applicationProcess = StringField()

	meta={
		'ordering': ['-metaData.yearValid']
	}