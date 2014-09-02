from rest_framework import serializers
from uniq.genericserializers import *

class ExploreSerializer(serializers.Serializer):
	id = serializers.CharField()
	name = serializers.CharField()
	images = ImageSerializer()
	undergradPopulation = serializers.CharField() 
	gradPopulation = serializers.CharField()
	location = LocationSerializer()