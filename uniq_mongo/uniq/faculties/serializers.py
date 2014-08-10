from uniq.genericserializers import *

class FacultySerializer(GenericSerializer):
	slug = serializers.CharField()
	schoolId = serializers.CharField()
	numPrograms = serializers.IntegerField()
	applicationProcess = serializers.CharField()
	importantDates = ImportantDateSerializer()
	streams = StreamSerializer()

	def restore_object(self, attrs, instance=None):
		if instance is not None:
			return super(FacultySerializer, self).build_instance(attrs)
		return Factory(**attrs)