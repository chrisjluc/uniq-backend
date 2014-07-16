from django.db import models
from schools.models import School

class BaseModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	toDelete = models.BooleanField(default=False)

	class Meta:
		abstract = True

class Faculty(BaseModel):
	schoolId = models.ForeignKey(School,related_name='faculty')
	name = models.CharField(max_length=64, default='',unique=True)
	population = models.PositiveIntegerField(blank=True)
	dateEstablished = models.DateField(blank=True,null=True)
	numPrograms = models.PositiveSmallIntegerField(default='0',blank=True)
	logoUrl = models.URLField(max_length=256, default='',blank=True)
	website = models.URLField(max_length=128, default='',blank=True)
	facebookLink = models.URLField(max_length=128, default='',blank=True)
	twitterLink = models.URLField(max_length=128, default='',blank=True)
	linkedinLink = models.URLField(max_length=128, default='',blank=True)
	alumniNumber = models.PositiveIntegerField(default=0,blank=True)
	totalFunding = models.DecimalField(default=0,max_digits=17,decimal_places=2)
	additionalInfo = models.TextField(blank=True)

	class Meta:
		ordering = ('created',)

	def save(self, *args, **kwargs):
		if self.name:
			self.name = self.name.strip()
		super(Faculty, self).save(*args, **kwargs)


class FacultyImage(BaseModel):
	facultyId = models.ForeignKey(Faculty,related_name='images')
	imageLink = models.URLField(max_length=256, default='',unique=True)
	descriptor = models.CharField(max_length=256, default='')

	class Meta:
		ordering = ('created',)

	def save(self, *args, **kwargs):
		if self.descriptor:
			self.descriptor = self.descriptor.strip()
		super(FacultyImage, self).save(*args, **kwargs)
