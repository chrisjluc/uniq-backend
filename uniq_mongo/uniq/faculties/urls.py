from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
	url(r'^schools/(?P<slug>[a-z]+)/faculties/$', views.FacultyList.as_view()),
	url(r'^schools/(?P<id>[A-z,0-9]+)/faculties/$', views.FacultyList.as_view()),
	url(r'^faculties/$', views.FacultyList.as_view()),
	url(r'^faculties/(?P<slug>[a-z]+)/$',views.FacultyDetail.as_view()),
	url(r'^faculties/(?P<id>[A-z,0-9]+)/$',views.FacultyDetail.as_view()),
)