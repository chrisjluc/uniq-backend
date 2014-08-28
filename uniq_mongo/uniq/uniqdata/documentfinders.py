from fieldfinders import *
from schools.models import School
from faculties.models import Faculty
from programs.models import Program

from django.http import Http404
import logging
import threading

#Keys
id='id'
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

streams = 'streams'
important_dates = 'importantDates'
deg = 'degree'
deg_abbr = 'degreeAbbrev'
internship = 'internship'

deg_req = 'degreeRequirements'
n_accepted = 'numAccepted'
n_app = 'numApplicants'
rating = 'rating'
requirements = 'requirements'


class SchoolFinder(object):
	
	def all(self):
		school_list = []
		schools_queried = {}

		schools = School.objects
		for school in schools:
			if school.slug not in schools_queried:
				schools_queried[school.slug] = True
				school_list.append(self.get(id=school.id))
		return school_list

	def explore(self):
		school_list = []
		schools_queried = {}

		schools = School.objects.only(id, name, images, u_pop ,g_pop ,location)
		for school in schools:
			if school.slug not in schools_queried:
				schools_queried[school.slug] = True
				self.school = school

		return school_list


	def get(self, slug = None, id = None):

		if id:
			self.school = School.objects.get(id=id)
		elif slug:
			self.school = School.objects(slug=slug).first()

		if not self.school:
			raise Http404

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

	def all(self, school_id = None, school_slug = None):

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
				faculty_list.append(self.get(id=faculty.id))
		return faculty_list

	def get(self, slug = None, school_id = None, id = None):

		if id:
			self.faculty = Faculty.objects.get(id=id)
		elif slug and school_id:
			self.faculty = Faculty.objects(slug=slug, schoolId=school_id).first()
		else:
			raise Exception("Invalid passed in parameters")

		if not self.faculty:
			raise Http404

		faculties = Faculty.objects(slug=self.faculty.slug, schoolId=self.faculty.schoolId, metaData__yearValid__lt=settings.CURRENT_YEAR)
		self.hist = HistoricalFieldFinder(faculties)
		self.hist_hierarchical = HistoricalHierarchicalFieldFinder(self.faculty, faculties)

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
		self.apply_hist_value(important_dates)
		self.apply_hist_hierarchical_value(contacts)
		self.apply_hist_value(images)
		self.apply_hist_value(rankings)
		self.apply_hist_hierarchical_value(location)

		self.apply_hist_value(deg)
		self.apply_hist_value(deg_abbr)
		self.apply_hist_value(internship)

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

class ProgramFinder(object):

	def all(self, faculty_id = None, school_slug = None, faculty_slug = None):

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
				program_list.append(self.get(id=program.id))
		return program_list

	def get(self, slug = None, faculty_id = None, id = None):

		if id:
			self.program = Program.objects.get(id=id)
		elif slug and faculty_id:
			self.program = Program.objects(slug=slug, facultyId=faculty_id).first()
		else:
			raise Exception("Invalid passed in parameters")

		if not self.program:
			raise Http404

		programs = Program.objects(slug=self.program.slug, facultyId=self.program.facultyId, metaData__yearValid__lt=settings.CURRENT_YEAR)
		self.hist = HistoricalFieldFinder(programs)
		self.hist_hierarchical = HistoricalHierarchicalFieldFinder(self.program, programs)

		self.apply_hist_value(name)
		self.apply_hist_value(short_name)
		self.apply_hist_value(about)
		self.apply_hist_hierarchical_value(app_process)
		self.apply_hist_value_with_year(u_pop)
		self.apply_hist_value_with_year(g_pop)
		self.apply_hist_value_with_year(avg_adm)
		self.apply_hist_value(date_est)

		self.apply_hist_hierarchical_value(streams)
		self.apply_hist_hierarchical_value(important_dates)
		self.apply_hist_hierarchical_value(contacts)
		self.apply_hist_value(images)
		self.apply_hist_value(rankings)
		self.apply_hist_hierarchical_value(location)

		self.apply_hist_hierarchical_value(deg)
		self.apply_hist_hierarchical_value(deg_abbr)
		self.apply_hist_hierarchical_value(internship)

		self.apply_hist_value(deg_req)
		self.apply_hist_value(n_accepted)
		self.apply_hist_value(n_app)
		self.apply_hist_value(rating)
		self.apply_hist_value(requirements)

		return self.program

	def apply_hist_value_with_year(self, key):
		if not self.program[key]:
			val = self.hist.find_value(key, True)
			if val:
				self.program[key] = val

	def apply_hist_value(self, key):
		if not self.program[key]:
			val = self.hist.find_value(key, False)
			if val:
				self.program[key] = val

	def apply_hist_hierarchical_value(self, key):
		if not self.program[key]:
			val = self.hist_hierarchical.find_value(key, False)
			if val:
				self.program[key] = val