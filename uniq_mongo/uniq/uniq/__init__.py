from uniqdb import UniqDb
from uniqdata.datainitializer import DataInitializer
import logging

logging.basicConfig()

db = UniqDb()
db.clearCollections()

di = DataInitializer()
di.run()