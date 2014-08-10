from pymongo import Connection

class UniqDb():
	def __init__(self,db_name = "mongoenginetest"):
		connection = Connection('localhost', 27017)
		self.db = connection[db_name]
	
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
