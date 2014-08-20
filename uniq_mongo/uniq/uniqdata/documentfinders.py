from fieldfinders import *
from schools.models import School
from faculties.models import Faculty
from programs.models import Program
import logging

class SchoolFinder(object):

	def __init__(self):
		self.Log = logging.getLogger(self.__class__.__name__)
		if id:
			self.id = id
			return
		elif slug:
			self.slug = slug
			return
		self.Log.error("Got initialized without id or slug")

	def get(self, slug = None, id = None):
		#Keys
		name = 'name'
		short_name = 'shortName'
		about = 'about'
		app_process = 'applicationProcess'
		u_pop = 'undergradPopulation'
		g_pop = 'gradPopulation'
		avg_adm = 'avgAdm'
		date_est = 'dateEstablished'
		num_fac = 'numFaculties'
		num_pro = 'numPrograms'
		contacts = 'contacts'
		images = 'images'
		rankings = 'rankings'
		location = 'location'

		self.school = None
		self.hist = None

		if id:
			self.school = School.objects.get(id=id)
		elif slug:
			self.school = School.objects(slug=slug).first()

		self.hist = HistoricalFieldFinder(School.objects(slug=self.school.slug, metaData__yearValid__lt=settings.CURRENT_YEAR))

		self.apply_hist_value(name)
		self.apply_hist_value(short_name)
		self.apply_hist_value(about)
		self.apply_hist_value_with_year(app_process)
		self.apply_hist_value_with_year(u_pop)
		self.apply_hist_value_with_year(g_pop)
		self.apply_hist_value_with_year(avg_adm)
		self.apply_hist_value(date_est)
		self.apply_hist_value_with_year(num_fac)
		self.apply_hist_value_with_year(num_pro)

		self.apply_hist_value(contacts)
		self.apply_hist_value(images)
		self.apply_hist_value(rankings)
		self.apply_hist_value(location)

		return self.school

	def apply_hist_value_with_year(self, key):
		if not self.school[key]:
			val = self.hist.find_value(key, True)
			if val:
				self.school[key] = val

	def apply_hist_value(self, key):
		if not self.school[key]:
			val = self.hist.find_value(key, False)
			if val:
				self.school[key] = val

class FacultyFinder(object):

	def __init__(self):
		self.Log = logging.getLogger(self.__class__.__name__)
		if id:
			self.id = id
			return
		elif slug:
			self.slug = slug
			return
		self.Log.error("Got initialized without id or slug")

	def get(self, slug = None, id = None):
		#Keys
		name = 'name'
		short_name = 'shortName'
		about = 'about'
		app_process = 'applicationProcess'
		u_pop = 'undergradPopulation'
		g_pop = 'gradPopulation'
		avg_adm = 'avgAdm'
		date_est = 'dateEstablished'
		num_pro = 'numPrograms'
		streams = 'streams'
		important_dates = 'importantDates'
		contacts = 'contacts'
		images = 'images'
		rankings = 'rankings'
		location = 'location'

		self.faculty = None
		self.hist = None

		if id:
			self.faculty = Faculty.objects.get(id=id)
		elif slug:
			self.faculty = Faculty.objects(slug=slug).first()

		faculties = Faculty.objects(slug=self.faculty.slug, metaData__yearValid__lt=settings.CURRENT_YEAR)
		self.hist = HistoricalFieldFinder(faculties)
		self.hist_hierarchical = HistoricalHierarchicalFieldFinder(faculty, faculties)

		self.apply_hist_value(name)
		self.apply_hist_value(short_name)
		self.apply_hist_value(about)
		self.apply_hist_hierarchical_value(app_process)
		self.apply_hist_value_with_year(u_pop)
		self.apply_hist_value_with_year(g_pop)
		self.apply_hist_value_with_year(avg_adm)
		self.apply_hist_value(date_est)
		self.apply_hist_value_with_year(num_pro)

		self.apply_hist_value(streams)
		self.apply_hist_value(importantDates)
		self.apply_hist_value(contacts)
		self.apply_hist_value(images)
		self.apply_hist_value(rankings)
		self.apply_hist_value(location)

		return self.faculty

	def apply_hist_value_with_year(self, key):
		if not self.faculty[key]:
			val = self.hist.find_value(key, True)
			if val:
				self.faculty[key] = val

	def apply_hist_value(self, key):
		if not self.faculty[key]:
			val = self.hist.find_value(key, False)
			if val:
				self.faculty[key] = val

	def apply_hist_hierarchical_value(self, key):
		if not self.faculty[key]:
			val = self.hist_hierarchical.find_value(key, False)
			if val:
				self.faculty[key] = val