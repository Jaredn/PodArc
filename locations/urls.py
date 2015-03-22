from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout_then_login
import locations.views

urlpatterns = patterns('',
    url(r'^$', locations.views.home, name='locations_home'),
    url(r'^index', locations.views.home,),
    url(r'^$', locations.views.home, name='locations_datacenter_create'),
    url(r'^$', locations.views.home, name='locations_cage_create'),
    url(r'^$', locations.views.home, name='locations_cagerow_create'),
    url(r'^$', locations.views.home, name='locations_rack_create'),
)