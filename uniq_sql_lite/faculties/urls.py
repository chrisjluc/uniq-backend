from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from faculties import views

urlpatterns = patterns('',
	url(r'^schools/(?P<schoolId>[0-9]+)/faculties/$', views.FacultiesInSchoolList.as_view()),
	url(r'^faculties/$', views.FacultyList.as_view()),
	url(r'^faculties/(?P<pk>[0-9]+)/$',views.FacultyDetail.as_view()),
	url(r'^faculties/update/(?P<timeLastModified>[0-9]+)/$',views.FacultyUpdate.as_view()),
	url(r'^faculties/image/$',views.FacultyImage.as_view()),

)
urlpatterns = format_suffix_patterns(urlpatterns)