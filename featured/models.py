from mongoengine import *

import datetime

class Featured(Document):
	'''
		Return only a certain number of featured items (depends on settings
		Order takes prescedent on priority then date created
	'''
	# Why it's featured
	featuredTitle = StringField()

	# Ex.
	# Mechatronics Engineering at University of Waterloo
	# University of Waterloo
	# Faculty of Engineering at University of Waterloo
	nameTitle = StringField()

	#TODO: Might not need this, in the future
	# program, faculty, school
	id = ObjectIdField()
	type = StringField()
	priority = IntField(default=100)
	dateCreated = DateTimeField(default=datetime.datetime.now())
	dateExpired = DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=7))
	imageLink = URLField()

	meta={
		'ordering': ['priority','-date_created']
	}
