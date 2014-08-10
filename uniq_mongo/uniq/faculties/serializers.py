from uniq.genericserializers import *

class FacultySerializer(GenericSerializer):
	slug = serializers.CharField()
	schoolId = serializers.CharField()
	numPrograms = serializers.IntegerField()
	applicationProcess = serializers.CharField()
	importantDates = ImportantDateSerializer()
	streams = StreamSerializer()