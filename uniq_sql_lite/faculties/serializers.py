from rest_framework import serializers
from faculties.models import Faculty,FacultyImage

#FACULTY IMAGE
class GetFacultyImageSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = FacultyImage
		fields = ('id','imageLink','descriptor')

class FacultyImageSuperUserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = FacultyImage

#FACULTY
class GetFacultySerializer(serializers.ModelSerializer):

	images = GetFacultyImageSerializer(many=True,required=False)
	
	class Meta:
		model = Faculty
		fields = ('id','name','population','location','dateEstablished','numPrograms',
			'logoUrl','website','facebookLink','twitterLink','linkedinLink',
			'alumniNumber','totalFunding','images','rankings')

class GetFacultySuperUserSerializer(serializers.ModelSerializer):
	
	images = FacultyImageSuperUserSerializer(many=True,required=False)

	class Meta:
		model = Faculty

class PostFacultySerializer(serializers.ModelSerializer):
	class Meta:
		model = Faculty