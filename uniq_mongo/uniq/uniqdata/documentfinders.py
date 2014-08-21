from fieldfinders import *
from schools.models import School
from faculties.models import Faculty
from programs.models import Program

from django.http import Http404
import logging

class SchoolFinder(object):
	
	@classmethod
	def all(cls):
		school_list = []
		schools = School.objects
		for school in schools:
			school_list.append(SchoolFinder.get(id=school.id))
		return school_list

	@classmethod
	def get(cls, slug = None, id = None):
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

		if id:
			cls.school = School.objects.get(id=id)
		elif slug:
			cls.school = School.objects(slug=slug).first()

		if not cls.school:
			raise Http404

		cls.hist = HistoricalFieldFinder(School.objects(slug=cls.school.slug, metaData__yearValid__lt=settings.CURRENT_YEAR))

		cls.apply_hist_value(name)
		cls.apply_hist_value(short_name)
		cls.apply_hist_value(about)
		cls.apply_hist_value_with_year(app_process)
		cls.apply_hist_value_with_year(u_pop)
		cls.apply_hist_value_with_year(g_pop)
		cls.apply_hist_value_with_year(avg_adm)
		cls.apply_hist_value(date_est)
		cls.apply_hist_value_with_year(num_fac)
		cls.apply_hist_value_with_year(num_pro)

		cls.apply_hist_value(contacts)
		cls.apply_hist_value(images)
		cls.apply_hist_value(rankings)
		cls.apply_hist_value(location)

		return cls.school

	@classmethod
	def apply_hist_value_with_year(cls, key):
		if not cls.school[key]:
			val = cls.hist.find_value(key, True)
			if val:
				cls.school[key] = val

	@classmethod
	def apply_hist_value(cls, key):
		if not cls.school[key]:
			val = cls.hist.find_value(key, False)
			if val:
				cls.school[key] = val

class FacultyFinder(object):

	@classmethod
	def all(cls, school_id = None, school_slug = None):

		faculties = None
		if school_id:
			school = School.objects.get(id=school_id)
			if not school:
				raise Http404
			faculties = Faculty.objects(schoolId=school.id)

		elif school_slug:
			school = School.objects(slug=school_slug).first()
			if not school:
				raise Http404
			faculties = Faculty.objects(schoolId=school.id)
		else:
			faculties = Faculty.objects

		faculty_list = []
		for faculty in faculties:
			faculty_list.append(FacultyFinder.get(id=faculty.id))
		return faculty_list

	@classmethod
	def get(cls, slug = None, school_id = None, id = None):
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

		if id:
			cls.faculty = Faculty.objects.get(id=id)
		elif slug and school_id:
			cls.faculty = Faculty.objects(slug=slug, schoolId=school_id).first()
		else:
			raise Exception("Invalid passed in parameters")

		if not cls.faculty:
			raise Http404

		faculties = Faculty.objects(slug=cls.faculty.slug, schoolId=cls.faculty.schoolId, metaData__yearValid__lt=settings.CURRENT_YEAR)
		cls.hist = HistoricalFieldFinder(faculties)
		cls.hist_hierarchical = HistoricalHierarchicalFieldFinder(cls.faculty, faculties)

		cls.apply_hist_value(name)
		cls.apply_hist_value(short_name)
		cls.apply_hist_value(about)
		cls.apply_hist_hierarchical_value(app_process)
		cls.apply_hist_value_with_year(u_pop)
		cls.apply_hist_value_with_year(g_pop)
		cls.apply_hist_value_with_year(avg_adm)
		cls.apply_hist_value(date_est)
		cls.apply_hist_value_with_year(num_pro)

		cls.apply_hist_value(streams)
		cls.apply_hist_value(important_dates)
		cls.apply_hist_hierarchical_value(contacts)
		cls.apply_hist_value(images)
		cls.apply_hist_value(rankings)
		cls.apply_hist_hierarchical_value(location)

		return cls.faculty

	@classmethod
	def apply_hist_value_with_year(cls, key):
		if not cls.faculty[key]:
			val = cls.hist.find_value(key, True)
			if val:
				cls.faculty[key] = val

	@classmethod
	def apply_hist_value(cls, key):
		if not cls.faculty[key]:
			val = cls.hist.find_value(key, False)
			if val:
				cls.faculty[key] = val

	@classmethod
	def apply_hist_hierarchical_value(cls, key):
		if not cls.faculty[key]:
			val = cls.hist_hierarchical.find_value(key, False)
			if val:
				cls.faculty[key] = val