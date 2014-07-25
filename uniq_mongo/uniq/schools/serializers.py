from uniq.genericserializers import *
from .models import School

class SchoolSerializer(GenericSerializer):
	
	numFaculties = serializers.IntegerField()
	numPrograms = serializers.IntegerField()
	applicationProcess = serializers.CharField()

