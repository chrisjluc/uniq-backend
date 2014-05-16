from django.db import models
from faculties.models import Faculty

TERM_CHOICES = (
	('1a', '1a'),
	('1b', '1b'),
	('2a', '2a'),
	('2b', '2b'),
	('3a', '3a'),
	('3b', '3b'),
	('4a', '4a'),
	('4b', '4b'),
	('5a', '5a'),
	('5b', '5b'),
	('UnSpec','Unspecified'),
	('N/a','N/A')
)
class BaseModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	toDelete = models.BooleanField(default=False)

	class Meta:
		abstract = True


class Program(BaseModel):
	name = models.CharField(max_length=64, default='',unique=True)
	degree = models.CharField(max_length=256,default='')
	population = models.PositiveIntegerField(blank=True)
	dateEstablished = models.DateField()
	about = models.TextField(blank=True)
	logoUrl = models.URLField(max_length=256, default='',blank=True)
	website = models.URLField(max_length=128, default='',blank=True)
	facebookLink = models.URLField(max_length=128, default='',blank=True)
	twitterLink = models.URLField(max_length=128, default='',blank=True)
	linkedinLink = models.URLField(max_length=128, default='',blank=True)
	alumniNumber = models.PositiveIntegerField(default=0,blank=True)
	totalFunding = models.DecimalField(default=0,max_digits=17,decimal_places=2)
	isCoop = models.BooleanField(default=True)
	numFavorites = models.PositiveIntegerField(blank=True,default=0)

	class Meta:
		ordering = ('created',)

	def save(self, *args, **kwargs):
		if self.name:
			self.name = self.name.strip()
		super(Program, self).save(*args, **kwargs)


class ProgramImage(BaseModel):
	
	programId = models.ForeignKey(Program,related_name='images')
	imageLink = models.URLField(max_length=256, default='',unique=True)
	descriptor = models.CharField(max_length=256, default='')

	class Meta:
		ordering = ('created',)

	def save(self, *args, **kwargs):
		if self.descriptor:
			self.descriptor = self.descriptor.strip()
		super(ProgramImage, self).save(*args, **kwargs)


class ProgramRanking(BaseModel):

	programId = models.ForeignKey(Program,related_name='rankings')
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
		super(ProgramRanking, self).save(*args, **kwargs)

class ProgramCourse(BaseModel):
	
	programId = models.ForeignKey(Program,related_name='courses')
	code = models.CharField(max_length=12, default='') #Take out all spaces when saving
	title = models.CharField(max_length=64, default='')
	description = models.CharField(max_length=2048, default='')
	term = models.CharField(choices=TERM_CHOICES,default='Unspecified')
	#per week
	classHour = models.DecimalField(default=0,max_digits=3,decimal_places=1,null=True)
	tutHour = models.DecimalField(default=0,max_digits=3,decimal_places=1,null=True)
	labHour = models.DecimalField(default=0,max_digits=3,decimal_places=1,null=True)
	
	class Meta:
		ordering = ('created',)


class ProgramFee(BaseModel):
	
	programId = models.ForeignKey(Program,related_name='fees')
	
	class Meta:
		ordering = ('created',)


class ProgramApplicationStat(BaseModel):

	programId = models.ForeignKey(Program,related_name='applicationStats')
	year = models.PositiveSmallIntegerField(unique=True)
	numApplicants = models.PositiveSmallIntegerField(blank=True)
	numAccepted = models.PositiveSmallIntegerField(blank=True)
	admissionDeadline = models.DateField(unique=True)

	class Meta:
		ordering = ('created',)


class ProgramImageLink(BaseModel):

	imageLink = models.URLField(max_length=256, default='',unique=True)
	descriptor = models.CharField(max_length=256, default='')
		
		class Meta:
		ordering = ('created',)


class ProgramRequirement(BaseModel):
		
		class Meta:
		ordering = ('created',)


class ProgramImportantDates(BaseModel):
		
		class Meta:
		ordering = ('created',)


class ProgramRating(BaseModel):
	"""
	This keeps the average of all ratings, each rating will be stored somehwere else and will update the averages
	"""
	programId = models.OneToOneField(Program,related_name='rating')