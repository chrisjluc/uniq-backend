from mongoengine import *
from programs.models import *
from faculties.models import *
from schools.models import *
from uniqdb import UniqDb

connect('mongoenginetest')
db = UniqDb()
# Initialize schema
if len(db.getCollectionNames()) == 0:
	s = School(slug="s")
	s.save()
	f = Faculty(slug="f",schoolId=s.id)
	f.save()
	p = Program(slug="p",schoolId=s.id, facultyId=f.id)
	p.save()
	db.clearCollections()