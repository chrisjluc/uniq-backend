from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('schools.urls')),
    url(r'^', include('faculties.urls')),
)
urlpatterns += patterns('',url(r'^api-auth/',include('rest_framework.urls',
	namespace='rest_framework')),
)