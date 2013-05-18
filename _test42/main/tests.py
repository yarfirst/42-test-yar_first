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
        
        self.failUnless(res.context['profile'])

        p = Profile.objects.all()[0]
        self.failUnless(res.content.find(p.name))

    def test_request_middleware(self):
        res = self.client.get('/requests/')
        self.assertEqual(res.status_code, 200)
        
        request_logs = RequestLog.objects.all().order_by('id')
        self.failUnless(request_logs)

        self.failUnless(res.context['request_logs'])
        
        context_request_logs = res.context['request_logs']
        
        log_length = len(context_request_logs)
        self.failUnless(log_length)
        self.failIf(log_length > 10)

        self.failUnless(res.content.find('/requests/'))

    def test_context_processor(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        
        self.failUnless(res.context['SETTINGS'])
        context_settings = res.context['SETTINGS']
        
        from django.conf import settings
        self.assertEqual(context_settings.DEBUG, settings.DEBUG)

    def test_edit_page(self):
        profile = Profile.objects.all()[0]
        
        profile_edit_url = '/edit/%s/' % profile.id
        
        res = self.client.get(profile_edit_url)
        self.assertEqual(res.status_code, 302)
        
        self.client.login(username='admin', password='admin')
        res = self.client.get(profile_edit_url)
        self.assertEqual(res.status_code, 200)

        self.failUnless(res.content.find('id_name'))
