from mongoengine import *
from uniq.genericmodels import GenericDocument

#db.school.save({_id:0,date_modified: new Date(), date_created:new Date()})
class School(GenericDocument):
	name = StringField(unique=True)
	slug = StringField(unique=True)