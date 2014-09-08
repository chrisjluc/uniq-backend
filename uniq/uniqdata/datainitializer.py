from datainterceptors import *
from schools.models import School
from faculties.models import Faculty
from programs.models import Program
import json
import os.path
import logging

class DataInitializer(object):

	mapping_path = "mapping.json"
	years_path = "validyears.json"

	def __init__(self, base_path = "./uniqdata/rawdata/"):
		self.Log = logging.getLogger(self.__class__.__name__)
		self.base_path = base_path
		data_path = base_path + self.mapping_path

		self.is_valid = True
		if os.path.isfile(data_path):
			with open(data_path) as data_file:
				self.mapping = json.load(data_file)
		else:
			self.is_valid = False
			self.Log.warning("Path to %s is not a valid file path" % self.base_path)

		base_years_path = base_path + self.years_path
		if os.path.isfile(base_years_path):
			with open(base_years_path) as data_file:
				self.years = json.load(data_file)['validyears']
		else:
			self.is_valid = False
			self.Log.warning("Path to %s is not a valid file path" % base_years_path)

	def run(self):
		if self.is_valid is False:
			return

		s_interceptor = GenericInterceptor()
		f_interceptor = FacultyInterceptor()
		p_interceptor = ProgramInterceptor()

		i = 0
		j = 0
		k = 0

		relatedProgramKeysById = {}

		# SCHOOL

		for school_slug, faculty_map in self.mapping.iteritems():

			for year in self.years:
				full_path = self.base_path + school_slug + "/" + school_slug + str(year) + '.json'

				data = None
				if os.path.isfile(full_path):
					with open(full_path) as data_file:
						data = json.load(data_file)
				else:
					continue

				data = s_interceptor.intercept(data)
				school = School(**data)
				school.save()
				self.Log.debug("School: %s has been saved." % school.name)
				i+=1

			school = School.objects(slug=school_slug).order_by("-metaData.yearValid").first()

			# FACULTY

			for faculty_slug, program_map in faculty_map.iteritems():
				
				for year in self.years:
					full_path = (self.base_path + school_slug + "/" 
						+ faculty_slug + "/" + faculty_slug + str(year) + '.json')

					data = None
					if os.path.isfile(full_path):
						with open(full_path) as data_file:
							data = json.load(data_file)
					else:
						continue

					data = f_interceptor.intercept(data, school.id)
					faculty = Faculty(**data)
					faculty.save()
					self.Log.debug("Faculty: %s has been saved." % faculty.name)
					j+=1

				faculty = Faculty.objects(slug=faculty_slug, schoolId = school.id).order_by("-metaData.yearValid").first()

				#PROGRAM

				for program_slug in program_map:
					# year: related program keys
					newestRelatedProgramKeys = {}

					for year in self.years:
						full_path = (self.base_path + school_slug + "/" 
							+ faculty_slug + "/" + program_slug + str(year) + '.json')

						data = None
						if os.path.isfile(full_path):
							with open(full_path) as data_file:
								data = json.load(data_file)
						else:
							continue

						if newestRelatedProgramKeys:
							if (newestRelatedProgramKeys.keys()[0] < year 
								and data.relatedProgramKeys is not None 
								and len(data.relatedProgramKeys) is not 0):

								newestRelatedProgramKeys = {}
								newestRelatedProgramKeys[year] = data['relatedProgramKeys']
						else:
							newestRelatedProgramKeys[year] = data['relatedProgramKeys']

						data = p_interceptor.intercept(data, school.id, faculty.id)
						program = Program(**data)
						program.save()
						self.Log.debug("Program: %s has been saved." % program.name)
						k+=1

					program = Program.objects(slug=program_slug, facultyId = faculty.id).order_by("-metaData.yearValid").first()
					relatedProgramKeysById[program.id] = newestRelatedProgramKeys[newestRelatedProgramKeys.keys()[0]]

		# Save related programs now that we have all ids

		for k,v in relatedProgramKeysById.iteritems():
			program = Program.objects.get(id=k)
			p_interceptor.related_intercept(program, v)

		self.Log.debug("# of school json files inserted: %s" % i)
		self.Log.debug("# of faculty json files inserted: %s" % j)
		self.Log.debug("# of program json files inserted: %s" % k)
