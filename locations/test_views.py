from django.test.client import Client
from django.http import HttpRequest
from django.test import TestCase
from django.core.urlresolvers import resolve, reverse

from locations.views import home, datacenter_create

class TestExamples(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+2, 3)


class TestLocationsViews(TestCase):

    def test_root_url_resolves(self):
        """ Check that url '/' resolves to home view """
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_admin_url(self):
        found = resolve('/admin/')
        self.assertEqual(found.app_name, 'admin')

    def test_all_views_resolve(self):
        #tuple of tuples... (View name, URL name to be tested against).  A resolve on the reverse of the view name should result in the URL name.
        view_list = (('locations.views.datacenter_create', 'locations_datacenter_create'),
                     ('locations.views.cage_create', 'locations_cage_create'),
                     ('locations.views.cagerow_create', 'locations_cagerow_create'),
                     ('locations.views.rack_create', 'locations_rack_create'),)
                    #todo: the views below require arguments...  need to fix the function to send arguments to test these views
                     # ('locations.views.datacenter_by_id', 'locations_datacenter_view_by_id'),
                     # ('locations.views.cage_by_id', 'locations_cage_view_by_id'),
                     # ('locations.views.cagerow_by_id', 'locations_cagerow_view_by_id'),
                     # ('locations.views.rack_by_id', 'locations_rack_view_by_id'))

        for item in view_list:
            print "testing ", item
            url = reverse(item[0])
            response = resolve(url)
            self.assertEqual(response.url_name, item[1])
            self.assertEqual(response.view_name, item[1])

    def test_datacenter_view_get(self):
        url = reverse('locations.views.datacenter_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_all_views_get(self):
        view_list = ('locations.views.datacenter_create', 'locations.views.cage_create', 'locations.views.cagerow_create',
                     'locations.views.rack_create')

        for item in view_list:
            print "testing ", item
            url = reverse(item)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_datacenter_view_post_create_datacenter(self):
        url = reverse('locations.views.datacenter_create')
        c = Client()
        response = c.post(url, dict(name='test datacenter', description=' a test datacenter'))
        #todo actually do an assertion here....
        print response.status_code
