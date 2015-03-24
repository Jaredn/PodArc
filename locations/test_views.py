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

    def test_datacenter_view_url(self):
        url = reverse('locations.views.datacenter_create')
        response = resolve(url)
        self.assertEqual(response.url_name, 'locations_datacenter_create')
        self.assertEqual(response.view_name, 'locations_datacenter_create')

    def test_datacenter_view_get(self):
        url = reverse('locations.views.datacenter_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_datacenter_view_post_create_datacenter(self):
        url = reverse('locations.views.datacenter_create')
        c = Client()
        response = c.post(url, dict(name='test datacenter', description=' a test datacenter'))
        print dir(response)

    def test_cage_view_url(self):
        url = reverse('locations.views.cage_create')
        response = resolve(url)
        self.assertEqual(response.url_name, 'locations_cage_create')
        self.assertEqual(response.view_name, 'locations_cage_create')

    def test_cage_view_get(self):
        url = reverse('locations.views.cage_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cagerow_view_url(self):
        url = reverse('locations.views.cagerow_create')
        response = resolve(url)
        self.assertEqual(response.url_name, 'locations_cagerow_create')
        self.assertEqual(response.view_name, 'locations_cagerow_create')

    def test_cagerow_view_get(self):
        url = reverse('locations.views.cagerow_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_rack_view_url(self):
        url = reverse('locations.views.rack_create')
        response = resolve(url)
        self.assertEqual(response.url_name, 'locations_rack_create')
        self.assertEqual(response.view_name, 'locations_rack_create')

    def test_rack_view_get(self):
        url = reverse('locations.views.rack_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
