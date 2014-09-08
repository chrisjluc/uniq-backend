from mongoengine import *
import datetime

class Location(EmbeddedDocument):
	address = StringField()
	apt = StringField()
	unit = StringField()
	city = StringField()
	region = StringField()
	postalCode = StringField()
	country = StringField()
	longitude = DecimalField()
	latitude = DecimalField()

class Meta(EmbeddedDocument):
	dateModified = DateTimeField(default=datetime.datetime.now)
	dateCreated = DateTimeField()
	yearValid = IntField()

class Image(EmbeddedDocument):
	descriptor = StringField()
	link = URLField()
	type = StringField()

class Ranking(EmbeddedDocument):
	year = IntField()
	rank = IntField()
	source = StringField()
	title = StringField()
	link = URLField()

class Stream(EmbeddedDocument):
	title = StringField()
	year1 = DynamicField()
	year2 = DynamicField()
	year3 = DynamicField()
	year4 = DynamicField()
	year5 = DynamicField()

class Fees(EmbeddedDocument):
	domestic = DynamicField()
	international = DynamicField()

class ImportantDate(EmbeddedDocument):
	date = StringField()
	type = StringField()
	description = StringField()

class Contact(EmbeddedDocument):
	name = StringField()
	email = EmailField()
	phoneNum = StringField()
	ext = StringField()
	fax = StringField()
	website = URLField()
	facebook = URLField()
	twitter = URLField()
	linkedin = URLField()
	extraInfo = StringField()

class Internship(EmbeddedDocument):
	general = StringField()
	specific = StringField()
	earnings = StringField()

class Related(EmbeddedDocument):
	relatedIds = ListField(StringField())
	relatedInfo = DynamicField()

class GenericDocument(Document):

	id = ObjectIdField()
	name = StringField()
	shortName = StringField()
	about = StringField()
	undergradPopulation = StringField()
	gradPopulation = StringField()
	applicationProcess = StringField()
	
	#Generic facts
	avgAdm = StringField()
	dateEstablished = DateTimeField()
	
	metaData = EmbeddedDocumentField(Meta)
	contacts = ListField(EmbeddedDocumentField(Contact))
	location = EmbeddedDocumentField(Location)
	rankings = ListField(EmbeddedDocumentField(Ranking))
	images = ListField(EmbeddedDocumentField(Image))

	meta = {
		'abstract': True
	}

