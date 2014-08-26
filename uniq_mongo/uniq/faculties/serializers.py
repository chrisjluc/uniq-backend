from uniq.genericserializers import *

class FacultySerializer(GenericSerializer):
	slug = serializers.CharField()
	schoolId = serializers.CharField()
	numPrograms = serializers.IntegerField()
	degree = serializers.CharField()
	degreeAbbrev = serializers.CharField()
	importantDates = ImportantDateSerializer()
	streams = StreamSerializer()
	internship = InternshipSerializer()

	def restore_object(self, attrs, instance=None):
		if instance is not None:
			return super(FacultySerializer, self).build_instance(attrs)
		return Factory(**attrs)