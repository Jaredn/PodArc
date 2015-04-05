from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout_then_login
import locations.views

urlpatterns = patterns('',
    url(r'^$', locations.views.home, name='locations_home'),
    url(r'^index', locations.views.home,),

    #Create "Locations"
    url(r'^datacenter/create$', locations.views.datacenter_create, name='locations_datacenter_create'),
    url(r'^cage/create$', locations.views.cage_create, name='locations_cage_create'),
    url(r'^cagerow/create$', locations.views.cagerow_create, name='locations_cagerow_create'),
    url(r'^rack/create$', locations.views.rack_create, name='locations_rack_create'),

    #View "Locations" (details)
    url(r'^datacenter/(?P<pk>\d+)$', locations.views.datacenter_by_id, name='locations_datacenter_view_by_id'),
    url(r'^cage/(?P<pk>\d+)/$', locations.views.cage_by_id, name='locations_cage_view_by_id'),
    url(r'^cagerow/(?P<pk>\d+)/$', locations.views.cagerow_by_id, name='locations_cagerow_view_by_id'),
    url(r'^rack/(?P<pk>\d+)/$', locations.views.rack_by_id, name='locations_rack_view_by_id'),
)