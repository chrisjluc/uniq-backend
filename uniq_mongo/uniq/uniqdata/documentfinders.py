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
		schools_queried = {}

		schools = School.objects
		for school in schools:
			if school.slug not in schools_queried:
				schools_queried[school.slug] = True
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
			faculties = Faculty.objects(schoolId=school_id)
		elif school_slug:
			school = School.objects(slug=school_slug).first()
			if not school:
				raise Http404
			faculties = Faculty.objects(schoolId=school.id)
		else:
			faculties = Faculty.objects

		faculty_list = []
		faculties_queried = {}

		for faculty in faculties:
			if faculty.slug not in faculties_queried:
				faculties_queried[faculty.slug] = True
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
		deg = 'degree'
		deg_abbr = 'degreeAbbrev'
		internship = 'internship'

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

		cls.apply_hist_value(deg)
		cls.apply_hist_value(deg_abbr)
		cls.apply_hist_value(internship)

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

class ProgramFinder(object):

	@classmethod
	def all(cls, faculty_id = None, school_slug = None, faculty_slug = None):

		programs = None
		if faculty_id:
			programs = Program.objects(facultyId=faculty_id)
		elif school_slug and faculty_slug:
			school = School.objects(slug=school_slug).first()
			if not school:
				raise Http404
			faculty = Faculty.objects(slug=faculty_slug, schoolId=school.id).first()
			if not faculty:
				raise Http404
			programs = Program.objects(facultyId=faculty.id)
		else:
			programs = Program.objects

		program_list = []
		program_queried = {}

		for program in programs:
			if program.slug not in program_queried:
				program_queried[program.slug] = True
				program_list.append(ProgramFinder.get(id=program.id))
		return program_list

	@classmethod
	def get(cls, slug = None, faculty_id = None, id = None):
		#Keys
		name = 'name'
		short_name = 'shortName'
		about = 'about'
		app_process = 'applicationProcess'
		u_pop = 'undergradPopulation'
		g_pop = 'gradPopulation'
		avg_adm = 'avgAdm'
		date_est = 'dateEstablished'
		streams = 'streams'
		important_dates = 'importantDates'
		contacts = 'contacts'
		images = 'images'
		rankings = 'rankings'
		location = 'location'

		deg = 'degree'
		deg_abbr = 'degreeAbbrev'
		fees = 'fees'
		internship = 'internship'


		#program specific
		deg_req = 'degreeRequirements'
		n_accepted = 'numAccepted'
		n_app = 'numApplicants'
		rating = 'rating'
		requirements = 'requirements'

		if id:
			cls.program = Program.objects.get(id=id)
		elif slug and faculty_id:
			cls.program = Program.objects(slug=slug, facultyId=faculty_id).first()
		else:
			raise Exception("Invalid passed in parameters")

		if not cls.program:
			raise Http404

		programs = Program.objects(slug=cls.program.slug, facultyId=cls.program.facultyId, metaData__yearValid__lt=settings.CURRENT_YEAR)
		cls.hist = HistoricalFieldFinder(programs)
		cls.hist_hierarchical = HistoricalHierarchicalFieldFinder(cls.program, programs)

		cls.apply_hist_value(name)
		cls.apply_hist_value(short_name)
		cls.apply_hist_value(about)
		cls.apply_hist_hierarchical_value(app_process)
		cls.apply_hist_value_with_year(u_pop)
		cls.apply_hist_value_with_year(g_pop)
		cls.apply_hist_value_with_year(avg_adm)
		cls.apply_hist_value(date_est)

		cls.apply_hist_hierarchical_value(streams)
		cls.apply_hist_hierarchical_value(important_dates)
		cls.apply_hist_hierarchical_value(contacts)
		cls.apply_hist_value(images)
		cls.apply_hist_value(rankings)
		cls.apply_hist_hierarchical_value(location)

		cls.apply_hist_hierarchical_value(deg)
		cls.apply_hist_hierarchical_value(deg_abbr)
		cls.apply_hist_hierarchical_value(internship)

		cls.apply_hist_value(deg_req)
		cls.apply_hist_value(n_accepted)
		cls.apply_hist_value(n_app)
		cls.apply_hist_value(rating)
		cls.apply_hist_value(requirements)

		return cls.program

	@classmethod
	def apply_hist_value_with_year(cls, key):
		if not cls.program[key]:
			val = cls.hist.find_value(key, True)
			if val:
				cls.program[key] = val

	@classmethod
	def apply_hist_value(cls, key):
		if not cls.program[key]:
			val = cls.hist.find_value(key, False)
			if val:
				cls.program[key] = val

	@classmethod
	def apply_hist_hierarchical_value(cls, key):
		if not cls.program[key]:
			val = cls.hist_hierarchical.find_value(key, False)
			if val:
				cls.program[key] = val