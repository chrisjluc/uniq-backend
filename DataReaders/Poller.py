import json
from mongoengine import *
from pprint import pprint
import time
from time import mktime
from datetime import datetime

schools = "waterloo.json"
faculties = "engineering.json"
database = 'mongoenginetest'

class School(DynamicDocument):
	name = StringField()

class Faculty(DynamicDocument):
	name = StringField()
	schoolId = ReferenceField(School)

class Program(DynamicDocument):
	name = StringField()

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
	school.contact = data['contact']
	school.images = data['images']
	school.rankings = data['rankings']
	school.location = data['location']
	school.metaData = data['meta']

	#set meta
	school.metaData['dateModified'] = datetime.utcnow()
	school.metaData['dateCreated'] = datetime.utcnow()
	struct = time.strptime(school.dateEstablished, "%d-%m-%Y")
	school.dateEstablished =  datetime.fromtimestamp(mktime(struct))
	
	school.save()
	print 'Successfully inserted {0} into {1}'.format(school.name, database)
	return school

def insertFaculty(data, school):

	faculty= Faculty(name=data['name'])
	faculty.shortName = data['shortName']
	faculty.slug = data['slug']
	faculty.about = data['about']
	faculty.undergradPopulation = data['undergradPopulation']
	faculty.gradPopulation = data['gradPopulation']
	faculty.avgAdm = data['avgAdm']
	faculty.numPrograms = data['numPrograms']
	faculty.dateEstablished = data['dateEstablished']
	faculty.contact = data['contact']
	faculty.images = data['images']
	faculty.rankings = data['rankings']
	faculty.location = data['location']
	faculty.metaData = data['meta']

	faculty.metaData['dateModified'] = datetime.utcnow()
	faculty.metaData['dateCreated'] = datetime.utcnow()
	struct = time.strptime(faculty.dateEstablished, "%d-%m-%Y")
	faculty.dateEstablished =  datetime.fromtimestamp(mktime(struct))
	
	faculty.schoolId = school
	faculty.save()
	print 'Successfully inserted {0} into {1}'.format(faculty.name, database)
	return faculty

try:
	connect('mongoenginetest')
	school = insertSchool(json.load(open(schools)))
	faculty = insertFaculty(json.load(open(faculties)), school)
except ValueError:
	print ValueError
