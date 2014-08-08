from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
	url(r'^faculties/(?P<slug>[a-z]+)/programs/$', views.ProgramList.as_view()),
	url(r'^faculties/(?P<id>[A-z,0-9]+)/programs/$', views.ProgramList.as_view()),
	url(r'^programs/$', views.ProgramList.as_view()),
	url(r'^programs/(?P<id>[A-z,0-9]+)/$',views.ProgramDetail.as_view()),
)