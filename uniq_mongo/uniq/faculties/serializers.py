from uniq.genericserializers import *

class FacultySerializer(GenericSerializer):
	
	numPrograms = serializers.IntegerField()
	schoolId = serializers.CharField()
