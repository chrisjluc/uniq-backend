from mongoengine import *
from programs.models import *
from faculties.models import *
from schools.models import *
from uniqdb import UniqDb
from uniqdata.datainitializer import DataInitializer
import settings
import logging


connect(settings.MONGO_DATABASE_NAME, host=settings.MONGO_HOST, port=settings.MONGO_PORT)
logging.basicConfig()

db = UniqDb()
db.clearCollections()

di = DataInitializer()
di.run()