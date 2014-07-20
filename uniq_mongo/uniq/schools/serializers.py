from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.Serializer):
	name = serializers.CharField()
	slug = serializers.CharField(required=False)
	date_modified = serializers.DateField(required=False)
	date_created = serializers.DateField(required=False)

	def restore_object(self, attrs, instance=None):
		if instance is not None:
			for k, v in attrs.iteritems():
				setattr(instance, k, v)
			return instance
		return School(**attrs)