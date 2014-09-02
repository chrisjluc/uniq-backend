from uniq.genericserializers import *
from .models import School

class SchoolSerializer(GenericSerializer):
	slug = serializers.CharField()
	numFaculties = serializers.IntegerField()
	numPrograms = serializers.IntegerField()

	def restore_object(self, attrs, instance=None):
		if instance is not None:
			return super(SchoolSerializer, self).build_instance(attrs)
		return School(**attrs)
