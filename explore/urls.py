from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
	url(r'^explore/schools/$', views.SchoolExplore.as_view()),
	url(r'^explore/faculties/$', views.FacultyExplore.as_view()),
	url(r'^explore/faculties/(?P<school_id>[a-f\d]{24})/$', views.FacultyExplore.as_view()),
	url(r'^explore/programs/$', views.ProgramExplore.as_view()),
	url(r'^explore/programs/(?P<faculty_id>[a-f\d]{24})/$', views.ProgramExplore.as_view()),

	url(r'^explore/program/(?P<id>[a-f\d]{24})/$', views.ProgramExploreDetail.as_view()),
)