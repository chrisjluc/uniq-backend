from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
	url(r'^schools/$', views.SchoolList.as_view()),
	url(r'^schools/(?P<slug>[a-z]+)/$',views.SchoolDetail.as_view()),
	url(r'^schools/(?P<id>[A-z,0-9]+)/$',views.SchoolDetail.as_view()),
)