from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
	url(r'^schools/(?P<school_slug>[a-z]+)/faculties/$', views.FacultyList.as_view()),
	url(r'^schools/(?P<school_id>[a-f\d]{24})/faculties/$', views.FacultyList.as_view()),
	url(r'^faculties/$', views.FacultyList.as_view()),
	
	url(r'^schools/(?P<school_slug>[a-z]+)/faculties/(?P<slug>[a-z]+)/$', views.FacultyDetail.as_view()),
	url(r'^faculties/(?P<id>[a-f\d]{24})/$',views.FacultyDetail.as_view()),
)