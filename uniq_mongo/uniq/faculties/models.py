from mongoengine import *
from schools.models import School
from uniq.genericmodels import *

class Faculty(GenericDocument):
	slug = StringField(unique_with=['schoolId', 'metaData.yearValid'])
	schoolId = ObjectIdField()
	numPrograms = StringField()
	degree = StringField()
	degreeAbbrev = StringField()
	streams = ListField(EmbeddedDocumentField(Stream))
	importantDates = ListField(EmbeddedDocumentField(ImportantDate))
	internship = EmbeddedDocumentField(Internship)
	

	meta={
		'ordering': ['-metaData.yearValid']
	}