from django.conf import settings

class HistoricalFieldFinder(object):
	'''
		Assume objects are given to it in newest to oldest
	'''

	def __init__(self, objects):
		self.objects = objects
	
	def find_value(self, key, append_year = False):
		for obj in self.objects:
			if obj['metaData']['yearValid'] >= settings.CURRENT_YEAR:
				continue
			if obj[key]:
				if append_year is True:
					year = str(obj['metaData']['yearValid'])
					return obj[key] + " ({0})".format(year)
				return obj[key]
		return None

