from mongoengine import *
from uniq.genericmodels import GenericDocument

class School(GenericDocument):
	slug = StringField(unique=True)
	numFaculties = StringField()
	numPrograms = StringField()
	applicationProcess = StringField()
