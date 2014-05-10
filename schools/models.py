from django.db import models

class BaseModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	toDelete = models.BooleanField(default=False)

	class Meta:
		abstract = True

class School(BaseModel):
	name = models.CharField(max_length=64, default='',unique=True)
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


	class Meta:
		ordering = ('created',)

	def save(self, *args, **kwargs):
		if self.name:
			self.name = self.name.strip()
		super(School, self).save(*args, **kwargs)

class Location(BaseModel):
	schoolId = models.OneToOneField(School,related_name='location',unique=True)
	streetNum = models.CharField(max_length=8, default='',blank=True)
	streetName = models.CharField(max_length=64, default='',blank=True)
	apt = models.PositiveIntegerField(default=None,blank=True)
	unit = models.PositiveIntegerField(default=None,blank=True)
	city = models.CharField(max_length=64, default='',blank=True)
	region = models.CharField(max_length=64, default='',blank=True)
	country = models.CharField(max_length=64, default='',blank=True)
	lattitude = models.DecimalField(default=0,blank=True,max_digits=11,decimal_places=8)
	longitude = models.DecimalField(default=0,blank=True,max_digits=11,decimal_places=8)

	class Meta:
		ordering = ('created',)

	def save(self, *args, **kwargs):
		if self.streetNum:
			self.streetNum = self.streetNum.strip()
		if self.streetName:
			self.streetName = self.streetName.strip()
		if self.city:
			self.city = self.city.strip()
		if self.region:
			self.region = self.region.strip()
		if self.country:
			self.country = self.country.strip()

		super(Location, self).save(*args, **kwargs)

class SchoolImage(BaseModel):
	schoolId = models.ForeignKey(School,related_name='images')
	imageLink = models.URLField(max_length=256, default='',unique=True)
	descriptor = models.CharField(max_length=256, default='')

	class Meta:
		ordering = ('created',)

	def save(self, *args, **kwargs):
		if self.descriptor:
			self.descriptor = self.descriptor.strip()
		super(SchoolImage, self).save(*args, **kwargs)

class SchoolRanking(BaseModel):
	schoolId = models.ForeignKey(School,related_name='rankings')
	ranking = models.PositiveIntegerField(default=None)
	rankingSource = models.CharField(max_length=256)
	descriptor = models.CharField(max_length=256,default='',blank=True)

	class Meta:
		ordering = ('created',)

	def save(self, *args, **kwargs):
		if self.rankingSource:
			self.rankingSource = self.rankingSource.strip()
		if self.descriptor:
			self.descriptor = self.descriptor.strip()
		super(SchoolRanking, self).save(*args, **kwargs)