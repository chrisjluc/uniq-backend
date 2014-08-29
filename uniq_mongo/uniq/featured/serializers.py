from rest_framework import serializers

class FeaturedSerializer(serializers.Serializer):
	featured_title = serializers.CharField()
	name_title = serializers.CharField()
	type = serializers.CharField()
	priority = serializers.IntegerField()
	date_created = serializers.DateTimeField()
	date_expired = serializers.DateTimeField()
	image_link = serializers.URLField()
