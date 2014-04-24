from django.db import models

class School(UniqModel):
	name = models.CharField(max_length=64, default='',blank=True,unique=True)
	population = models.PositiveIntegerField(blank=True)
	dateEstablished = models.DateField()
	numPrograms = models.PositiveSmallIntegerField(default='0',blank=True)
	logoUrl = models.URLField(max_length=256, default='',blank=True)
	website = models.URLField(max_length=128, default='',blank=True)
	facebookLink = models.URLField(max_length=128, default='',blank=True)
	twitterLink = models.URLField(max_length=128, default='',blank=True)
	linkedinLink = models.URLField(max_length=128, default='',blank=True)
	alumniNumber = models.PositiveIntegerField(default=0,blank=True)
	totalFunding = models.DecimalField(default=0,max_digits=17,decimal_places=2)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	toDelete = models.BooleanField(default=False)

	class Meta:
		ordering = ('name',)

class Location(UniqModel):
	schoolId = models.ForeignKey(School,related_name='location',unique=True)
	streetNum = models.CharField(max_length=8, default='',blank=True)
	streetName = models.CharField(max_length=64, default='',blank=True)
	apt = models.PositiveIntegerField(default=None,blank=True)
	unit = models.PositiveIntegerField(default=None,blank=True)
	city = models.CharField(max_length=64, default='',blank=True)
	region = models.CharField(max_length=64, default='',blank=True)
	country = models.CharField(max_length=64, default='',blank=True)
	lattitude = models.DecimalField(default=None,blank=True,max_digits=11,decimal_places=8)
	longitude = models.DecimalField(default=None,blank=True,max_digits=11,decimal_places=8)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	toDelete = models.BooleanField(default=False)

	class Meta:
		ordering = ('created',)

class SchoolImage(UniqModel):
	schoolId = models.ForeignKey(School,related_name='images')
	imageLink = models.URLField(max_length=256, default='',unique=True)
	descriptor = models.CharField(max_length=256, default='')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	toDelete = models.BooleanField(default=False)

	class Meta:
		ordering = ('created',)
