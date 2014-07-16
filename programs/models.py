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
DATA_TYPE = (('text','text'),('html','html'))

VALUE_TYPE = (('text','text'),('html','html'))#('competition','admission_info','event','admission_deadline')

class BaseModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	toDelete = models.BooleanField(default=False)

	class Meta:
		abstract = True


class Program(BaseModel):
	name = models.CharField(max_length=64, default='',unique=True)
	year = models.PositiveSmallIntegerField(unique=True)
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

class ProgramImage(BaseModel):
	
	programId = models.ForeignKey(Program,related_name='images')
	imageLink = models.URLField(max_length=256, default='',unique=True)
	descriptor = models.CharField(max_length=256, default='')

	class Meta:
		ordering = ('created',)

class ProgramRank(BaseModel):

	programId = models.ForeignKey(Program,related_name='rankings')
	year = models.PositiveSmallIntegerField(unique=True)
	rank = models.DecimalField(default=0,max_digits=6,decimal_places=3)
	source = models.CharField(max_length=256)
	title = models.CharField(max_length=256,default='',blank=True)

	class Meta:
		ordering = ('created',)

class ProgramCourse(BaseModel):
	
	programId = models.ForeignKey(Program,related_name='courses')
	year = models.PositiveSmallIntegerField(unique=True)
	school_course_id = models.CharField(max_length=64, blank=True)
	code = models.CharField(max_length=12) #Take out all spaces when saving
	title = models.CharField(max_length=64)
	description = models.CharField(max_length=2048)
	term = models.CharField(choices=TERM_CHOICES,default='Unspecified',max_length=128)
	unit = models.DecimalField(default=0,max_digits=3,decimal_places=1)
	classHour = models.DecimalField(default=0,max_digits=3,decimal_places=1)
	tutHour = models.DecimalField(default=0,max_digits=3,decimal_places=1,)
	labHour = models.DecimalField(default=0,max_digits=3,decimal_places=1)
	
	class Meta:
		ordering = ('created',)


class ProgramTuition(BaseModel):
	
	programId = models.OneToOneField(Program,related_name='fees')
	#Yearly tuition by year 1:123123, 2:123123...
	class Meta:
		ordering = ('created',)


class ProgramApplicationStat(BaseModel):

	programId = models.ForeignKey(Program,related_name='applicationStats')
	year = models.PositiveSmallIntegerField(unique=True)
	numApplicants = models.PositiveSmallIntegerField(blank=True)
	numAccepted = models.PositiveSmallIntegerField(blank=True)
	#hold in % for ex. 90.5%
	admission_avg = models.DecimalField(default=0,max_digits=5,decimal_places=2)

	class Meta:
		ordering = ('created',)


class ProgramRequirement(BaseModel):
	
	courses = models.TextField()
	general = models.TextField()
	other = models.TextField()

	class Meta:
		ordering = ('created',)


class ProgramDates(BaseModel):
	
	programId = models.ForeignKey(Program,related_name='dates')
	year = models.PositiveSmallIntegerField(unique=True)
	date = models.DateField()
	value = models.CharField(default='',max_length=2048)
	valueType = models.CharField(choices=VALUE_TYPE,default='',max_length=128)
	datatype = models.CharField(choices=DATA_TYPE,default='TEXT',max_length=128)

	class Meta:
		ordering = ('created',)

#This keeps the average of all ratings,
# each rating will be stored somehwere else and will update the averages out of a 100

class ProgramRating(BaseModel):
	programId = models.OneToOneField(Program,related_name='rating')
	ratingOverall = models.PositiveSmallIntegerField()
	professors = models.PositiveSmallIntegerField()
	difficulty = models.PositiveSmallIntegerField()
	schedule = models.PositiveSmallIntegerField()
	classmates = models.PositiveSmallIntegerField()
	socialEnjoyment = models.PositiveSmallIntegerField()
	studyEnv = models.PositiveSmallIntegerField()
	guyRatio = models.PositiveSmallIntegerField()
 

	class Meta:
		ordering = ('created',)