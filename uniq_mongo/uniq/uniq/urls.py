from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('schools.urls')),
    url(r'^', include('faculties.urls')),
    url(r'^', include('programs.urls')),
    url(r'^', include('explore.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
