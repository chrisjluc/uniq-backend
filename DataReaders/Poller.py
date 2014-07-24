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
	return school.id

def insertfaculty(data):

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
	return school.id

connect('mongoenginetest')
school_id = insertSchool(json.load(open(file_name)))