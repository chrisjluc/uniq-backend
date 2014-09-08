from rest_framework import serializers
from uniq.genericserializers import *

class RequirementsSerializer(EmbeddedDocumentSerializer):
	province = serializers.CharField()
	average = serializers.CharField()
	individual_courses = serializers.CharField()
	list_courses = serializers.CharField()
	recommended_courses = serializers.CharField()
	general_requirements = serializers.CharField()
	notes = serializers.CharField()
	transfer_credits = serializers.CharField()
	other_documentation = ListSerializer()
	country = serializers.CharField()
	system_of_study = serializers.CharField()
	international_program_requirements = serializers.CharField()
	ap = serializers.CharField()

	def field_to_native(self, obj, field_name):
		if obj is None or obj.requirements is None:
			return None
		return self.to_native(obj.requirements)

class RatingSerializer(EmbeddedDocumentSerializer):
	ratingOverall = serializers.IntegerField()
	professors = serializers.IntegerField()
	difficulty = serializers.IntegerField()
	schedule = serializers.IntegerField()
	classmates = serializers.IntegerField()
	socialEnjoyment = serializers.IntegerField()
	studyEnv = serializers.IntegerField()
	guyRatio = serializers.IntegerField()

	def field_to_native(self, obj, field_name):
		if obj is None or obj.rating is None:
			return None
		return self.to_native(obj.rating)

class DegreeRequirementsSerializer(EmbeddedDocumentSerializer):
	about = serializers.CharField()
	curriculumTerms = ListSerializer()
	curriculum = EmbeddedDocumentSerializer()

	def field_to_native(self, obj, field_name):
		if obj is None or obj.degreeRequirements is None:
			return None
		return self.to_native(obj.degreeRequirements)

class ProgramSerializer(GenericSerializer):
	slug = serializers.CharField()
	schoolId = serializers.CharField()
	facultyId = serializers.CharField()
	degree = serializers.CharField()
	degreeAbbrev = serializers.CharField()
	numApplicants = serializers.CharField()
	numAccepted = serializers.CharField()

	requirements = RequirementsSerializer()
	streams = StreamSerializer()
	importantDates = ImportantDateSerializer()
	fees = FeeSerializer()
	rating = RatingSerializer()
	internship = InternshipSerializer()
	degreeRequirements = DegreeRequirementsSerializer()
	related = RelatedSerializer()

	def restore_object(self, attrs, instance=None):
		if instance is not None:
			return super(ProgramSerializer, self).build_instance(attrs)
		return Program(**attrs)

