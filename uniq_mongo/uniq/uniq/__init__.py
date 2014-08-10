from mongoengine import *
from programs.models import *
from faculties.models import *
from schools.models import *
from uniqdb import UniqDb
import settings

connect(settings.MONGO_DATABASE_NAME, host=settings.MONGO_HOST, port=settings.MONGO_PORT)
db = UniqDb()
# Initialize schema
if len(db.getCollectionNames()) == 0:
	s = School(slug="s_init")
	s.save()
	f = Faculty(slug="f_init",schoolId=s.id)
	f.save()
	p = Program(slug="p_init",schoolId=s.id, facultyId=f.id)
	p.save()
	db.clearCollections()