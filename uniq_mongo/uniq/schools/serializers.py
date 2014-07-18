from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.Serializer):
    school_id = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            for k, v in attrs.iteritems():
                setattr(instance, k, v)
            return instance
        return School(**attrs)