"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from models import Profile, RequestLog


class Test(TestCase):

    fixtures = ['initial_data.json']

    def test_profile_exists(self):
        profiles = Profile.objects.all()
        profiles = list(profiles)
        self.failUnless(profiles)

        p = profiles[0]
        self.failUnlessEqual(p.name, 'Some name')

    def test_profile_page(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

        self.failUnless('profile' not in res.context)

        p = Profile.objects.get(id=1)
        self.failUnless(res.content.find(p.name))

    def test_request_middleware(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        
        request_count = RequestLog.objects.count()
        self.failUnless(request_count)
