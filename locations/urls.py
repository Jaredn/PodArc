from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout_then_login
import locations.views

urlpatterns = patterns('',
    url(r'^$', locations.views.home, name='locations_home'),
    url(r'^index', locations.views.home,),
    url(r'^datacenter/create$', locations.views.datacenter_create, name='locations_datacenter_create'),
    url(r'^cage/create$', locations.views.cage_create, name='locations_cage_create'),
    url(r'^cagerow/create$', locations.views.cagerow_create, name='locations_cagerow_create'),
    url(r'^rack/create$', locations.views.rack_create, name='locations_rack_create'),

    #Location Views...
    url(r'^datacenter/(?P<pk>\d+)$', locations.views.datacenter_by_id, name='locations_rack_create'),
)