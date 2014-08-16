from pymongo import Connection
import settings

class UniqDb():
	def __init__(self):
		connection = Connection(settings.MONGO_HOST, settings.MONGO_PORT)
		self.db = connection[settings.MONGO_DATABASE_NAME]
	
	def getCollectionNames(self):
		return self.db.collection_names()
	
	def clearCollections(self):
		try:
			for name in self.db.collection_names():
				if name == "system.indexes":
					continue
				self.db[name].remove()
				print "Collections removed : {0}".format(name)
		except:
			print ("Failed to remove all records!")
