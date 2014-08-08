import json
from mongoengine import *
from pprint import pprint
import time
from time import mktime
from datetime import datetime

schools = "waterloo.json"
faculties = "engineering.json"
programs = "mechatronics.json"
database = 'mongoenginetest'

class School(DynamicDocument):
	name = StringField()

class Faculty(DynamicDocument):
	name = StringField()
	schoolId = ObjectIdField()

class Program(DynamicDocument):
	name = StringField()
	schoolId = ObjectIdField()
	facultyId = ObjectIdField()

def insertSchool(data):

	school = School(name=data['name'])
	school.shortName = data['shortName']
	school.slug = data['slug']
	school.about = data['about']
	school.applicationProcess = data['applicationProcess']
	school.undergradPopulation = data['undergradPopulation']
	school.gradPopulation = data['gradPopulation']
	school.avgAdm = data['avgAdm']
	school.dateEstablished = data['dateEstablished']
	school.numFaculties = data['numFaculties']
	school.numPrograms = data['numPrograms']
	school.contacts = data['contacts']
	school.images = data['images']
	school.rankings = data['rankings']
	school.location = data['location']
	school.metaData = data['meta']

	#set meta
	school.metaData['dateModified'] = datetime.utcnow()
	school.metaData['dateCreated'] = datetime.utcnow()
	struct = time.strptime(school.dateEstablished, "%d-%m-%Y")
	school.dateEstablished = datetime.fromtimestamp(mktime(struct))
	
	school.save()
	print 'Successfully inserted {0} into {1}'.format(school.name, database)
	return school.id

def insertFaculty(data, schoolId):

	faculty= Faculty(name=data['name'])
	faculty.shortName = data['shortName']
	faculty.slug = data['slug']
	faculty.about = data['about']
	faculty.undergradPopulation = data['undergradPopulation']
	faculty.gradPopulation = data['gradPopulation']
	faculty.avgAdm = data['avgAdm']
	faculty.numPrograms = data['numPrograms']
	faculty.dateEstablished = data['dateEstablished']
	faculty.applicationProcess = data['applicationProcess']
	faculty.streams = data['streams']
	faculty.contacts = data['contacts']
	faculty.images = data['images']
	faculty.rankings = data['rankings']
	faculty.location = data['location']
	faculty.metaData = data['meta']

	faculty.metaData['dateModified'] = datetime.utcnow()
	faculty.metaData['dateCreated'] = datetime.utcnow()
	struct = time.strptime(faculty.dateEstablished, "%d-%m-%Y")
	faculty.dateEstablished = datetime.fromtimestamp(mktime(struct))
	
	faculty.schoolId = schoolId
	faculty.save()
	print 'Successfully inserted {0} into {1}'.format(faculty.name, database)
	return faculty.id

def insertProgram(data, schoolId, facultyId):

	program= Program(name=data['name'])
	program.shortName = data['shortName']
	program.slug = data['slug']
	program.about = data['about']
	program.undergradPopulation = data['undergradPopulation']
	program.gradPopulation = data['gradPopulation']
	program.avgAdm = data['avgAdm']
	program.dateEstablished = data['dateEstablished']
	program.contacts = data['contacts']
	program.images = data['images']
	program.rankings = data['rankings']
	program.location = data['location']
	program.metaData = data['meta']
	program.metaData['dateModified'] = datetime.utcnow()
	program.metaData['dateCreated'] = datetime.utcnow()
	struct = time.strptime(program.dateEstablished, "%d-%m-%Y")
	program.dateEstablished = datetime.fromtimestamp(mktime(struct))
	
	program.degree = data['degree']
	program.degreeAbbrev = data['degreeAbbrev']
	program.numApplicants = data['numApplicants']
	program.numAccepted = data['numAccepted']
	program.requirements = data['requirements']
	program.streams = data['streams']
	program.fees = data['fees']
	program.rating = data['rating']
	program.internship = data['internship']
	program.importantDates = data['importantDates']
	program.degreeRequirements = data['degreeRequirements']

	program.schoolId = schoolId
	program.facultyId = facultyId
	program.save()
	print 'Successfully inserted {0} into {1}'.format(program.name, database)
	return program.id

connect('mongoenginetest')
school = None
faculty = None
program = None

schoolId = insertSchool(json.load(open(schools)))
facultyId = insertFaculty(json.load(open(faculties)), schoolId)
program = insertProgram(json.load(open(programs)), schoolId, facultyId)

