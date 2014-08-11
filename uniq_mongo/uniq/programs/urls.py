from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
	url(r'^schools/(?P<school_slug>[a-z]+)/faculties/(?P<faculty_slug>[a-z]+)/programs/$', views.ProgramList.as_view()),
	url(r'^faculties/(?P<faculty_id>[a-f\d]{24})/programs/$', views.ProgramList.as_view()),
	url(r'^programs/$', views.ProgramList.as_view()),

	url(r'^schools/(?P<school_slug>[a-z]+)/faculties/(?P<faculty_slug>[a-z]+)/programs/(?P<slug>[a-z]+)/$', views.ProgramDetail.as_view()),
	url(r'^programs/(?P<id>[a-f\d]{24})/$',views.ProgramDetail.as_view()),
)