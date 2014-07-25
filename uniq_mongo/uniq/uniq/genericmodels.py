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

class Contact(EmbeddedDocument):
	name = StringField()
	email = EmailField()
	phoneNumber = StringField()
	ext = StringField()
	fax = StringField()
	website = URLField()
	facebook = URLField()
	twitter = URLField()
	linkedin = URLField()

class Meta(EmbeddedDocument):
	dateModified = DateTimeField(default=datetime.datetime.now)
	dateCreated = DateTimeField()
	yearValid = IntField()

#db.school.update({"slug":"universityofwaterloo"},{$set:{image:{descriptor:"hello"}}})
class Image(EmbeddedDocument):
	descriptor = StringField()
	link = URLField()

class Ranking(EmbeddedDocument):
	year = IntField()
	rank = IntField()
	source = StringField()
	title = StringField()
	link = URLField()

class GenericDocument(Document):

	id = StringField()
	dateEstablished = DateTimeField()
	name = StringField(unique=True)
	shortName = StringField()
	slug = StringField(unique=True)
	about = StringField()
	undergradPopulation = IntField()
	gradPopulation = IntField()
	#Generic facts
	avgAdm = DecimalField()
	dateEstablished = DateTimeField()
	
	metaData = EmbeddedDocumentField(Meta)
	contact = EmbeddedDocumentField(Contact)
	location = EmbeddedDocumentField(Location)
	rankings = ListField(EmbeddedDocumentField(Ranking))
	images = ListField(EmbeddedDocumentField(Image))

	meta = {
		'abstract': True
	}

