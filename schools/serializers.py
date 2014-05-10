from rest_framework import serializers
from schools.models import School,Location,SchoolImage,SchoolRanking

#LOCATION
class GetLocationSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Location
		fields = ('streetNum','streetName','apt','unit',
			'city','region','country','lattitude','longitude')

class LocationSuperUserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Location

#SCHOOL IMAGE
class GetSchoolImageSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = SchoolImage
		fields = ('id','imageLink','descriptor')

class SchoolImageSuperUserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = SchoolImage

#SCHOOL RANKING
class GetSchoolRankingSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = SchoolRanking
		fields = ('id','ranking','rankingSource','descriptor')

class SchoolRankingSuperUserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = SchoolRanking

#SCHOOL
class GetSchoolSerializer(serializers.ModelSerializer):
	images = GetSchoolImageSerializer(many=True,required=False)
	location = GetLocationSerializer(required=False)
	rankings = GetSchoolRankingSerializer(many=True,required=False)
	
	class Meta:
		model = School
		fields = ('id','name','population','location','dateEstablished','numPrograms',
			'logoUrl','website','facebookLink','twitterLink','linkedinLink',
			'alumniNumber','totalFunding','images','rankings')

class GetSchoolSuperUserSerializer(serializers.ModelSerializer):
	
	location = LocationSuperUserSerializer(required=False)
	images = SchoolImageSuperUserSerializer(many=True,required=False)
	rankings = SchoolRankingSuperUserSerializer(many=True,required=False)

	class Meta:
		model = School

class PostSchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School