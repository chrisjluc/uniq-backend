from mongoengine import *
from schools.models import School
from uniq.genericmodels import GenericDocument, Stream, Fees, ImportantDate

class Requirements(EmbeddedDocument):
	province = StringField()
	average = StringField()
	individual_courses = DynamicField()
	list_courses = StringField()
	recommended_courses = StringField()
	general_requirements = StringField()
	notes = StringField()
	transfer_credits = StringField()
	other_documentation = ListField(StringField())
	country = StringField()
	system_of_study = StringField()
	international_program_requirements = StringField()
	ap = StringField()

class Rating(EmbeddedDocument):
	ratingOverall = IntField()
	professors = IntField()
	difficulty = IntField()
	schedule = IntField()
	classmates = IntField()
	socialEnjoyment = IntField()
	studyEnv = IntField()
	guyRatio = IntField()

class Internship(EmbeddedDocument):
	general = StringField()
	specific = StringField()
	earnings = StringField()

class DegreeRequirements(EmbeddedDocument):
	about = StringField()
	curriculumTerms = ListField(StringField())
	curriculum = DynamicField()

class Program(GenericDocument):
	slug = StringField(unique_with=['schoolId', 'facultyId', 'metaData.yearValid'])
	schoolId = ObjectIdField()
	facultyId = ObjectIdField()
	degree = StringField()
	degreeAbbrev = StringField()
	numApplicants = StringField()
	numAccepted = StringField()
	
	requirements = EmbeddedDocumentField(Requirements)
	streams = ListField(EmbeddedDocumentField(Stream))
	importantDates = ListField(EmbeddedDocumentField(ImportantDate))
	fees = EmbeddedDocumentField(Fees)
	rating = EmbeddedDocumentField(Rating)
	internship = EmbeddedDocumentField(Internship)
	degreeRequirements = EmbeddedDocumentField(DegreeRequirements)

	meta={
		'ordering': ['-metaData.yearValid']
	}