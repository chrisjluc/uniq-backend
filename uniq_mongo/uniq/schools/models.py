from mongoengine import *
from uniq.genericmodels import GenericDocument

class School(GenericDocument):
	slug = StringField(unique=True)
	numFaculties = IntField()
	numPrograms = IntField()
	applicationProcess = StringField()
