from mongoengine import *
from uniq.genericmodels import GenericDocument

class School(GenericDocument):
	slug = StringField(unique_with='metaData.yearValid')
	numFaculties = StringField()
	numPrograms = StringField()
	applicationProcess = StringField()

	meta={
		'ordering': ['-metaData.yearValid']
	}
