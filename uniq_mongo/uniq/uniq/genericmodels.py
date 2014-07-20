from mongoengine import *
import datetime

class GenericDocument(Document):
	date_modified = DateTimeField(default=datetime.datetime.now)
	date_created = DateTimeField(default=datetime.datetime.now)

	meta = {
		'abstract': True
	}

class Location(EmbeddedDocument):
	streetNum = StringField()
	streetName = StringField()
	apt = StringField()
	unit = StringField()
	city = StringField()
	region = StringField()
	country = StringField()
	geolocation = GeoPointField()

class Contact(EmbeddedDocument):
	email = EmailField()
	phoneNumber = StringField()
	fax = StringField()
	website = URLField()
	facebookLink = URLField()
	twitterLink = URLField()
	linkedinLink = URLField()

class Image(EmbeddedDocument):
	imageLink = URLField()
	descriptor = StringField()