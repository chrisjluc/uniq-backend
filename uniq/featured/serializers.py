from rest_framework import serializers

class FeaturedSerializer(serializers.Serializer):
	featuredTitle = serializers.CharField()
	nameTitle = serializers.CharField()
	id = serializers.CharField()
	type = serializers.CharField()
	priority = serializers.IntegerField()
	dateCreated = serializers.DateTimeField()
	dateExpired= serializers.DateTimeField()
	imageLink = serializers.URLField()
