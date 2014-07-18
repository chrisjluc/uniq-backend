from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from schools import views

urlpatterns = patterns('',
	url(r'^', views.SchoolList.as_view()),
)