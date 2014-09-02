from mongoengine import *

import datetime

class Featured(Document):
	'''
		Return only a certain number of featured items (depends on settings
		Order takes prescedent on priority then date created
	'''
	# Why it's featured
	featured_title = StringField()

	# Ex.
	# Mechatronics Engineering at University of Waterloo
	# University of Waterloo
	# Faculty of Engineering at University of Waterloo
	name_title = StringField()

	#TODO: Might not need this, in the future
	# program, faculty, school
	type = StringField()
	priority = IntField(default=100)
	date_created = DateTimeField(default=datetime.datetime.now())
	date_expired = DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=7))
	image_link = URLField()

	meta={
		'ordering': ['priority','-date_created']
	}
