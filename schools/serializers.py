from rest_framework import serializers
from schools.models import School,Location,SchoolImage

#LOCATION
class GetLocationSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Location
		fields = ('streetNum','streetName','apt','unit',
			'city','region','country','lattitude','longitude')

class PostLocationSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Location
		fields = ('schoolId','streetNum','streetName','apt','unit',
			'city','region','country','lattitude','longitude')

#SCHOOL IMAGE
class GetSchoolImageSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = SchoolImage
		fields = ('imageLink','descriptor')

class PostSchoolImageSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = SchoolImage
		fields = ('schoolId','imageLink','descriptor')

#SCHOOL
class GetSchoolSerializer(serializers.ModelSerializer):
	images = GetSchoolImageSerializer(many=True,required=False)
	location = GetLocationSerializer(required=False)
	
	class Meta:
		model = School
		fields = ('id','name','population','location','dateEstablished','numPrograms',
			'logoUrl','website','facebookLink','twitterLink','linkedinLink',
			'alumniNumber','totalFunding','images')

class PostSchoolSerializer(serializers.ModelSerializer):

	class Meta:
		model = School
		fields = ('name','population','dateEstablished','numPrograms',
			'logoUrl','website','facebookLink','twitterLink','linkedinLink',
			'alumniNumber','totalFunding')