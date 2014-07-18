from mongoengine import *

class School(Document):
	school_id = IntField(unique=True)
