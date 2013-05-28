"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import sys
from StringIO import StringIO

from django.core.management import call_command
from django.test import TestCase

from models import Profile, RequestLog, ModelChangesLog


class Test(TestCase):

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
        self.failUnless(res.content.find('edit_in_admin'))

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

        data = profile.__dict__
        data['name'] = 'TEST NAME'
        res = self.client.post(profile_edit_url, data)
        self.assertEqual(res.status_code, 302)

        profile = Profile.objects.all()[0]
        self.assertEqual(profile.name, data['name'])

    def test_project_models_command(self):
        stdout_orig = sys.stdout
        stderr_orig = sys.stderr

        sys.stdout = _stdout = StringIO()
        sys.stderr = _stderr = StringIO()

        call_command('project_models')

        sys.stdout = stdout_orig
        sys.stderr = stderr_orig

        _stdout.seek(0)
        _stderr.seek(0)

        _out_text = _stdout.read()
        _err_text = _stderr.read()

        self.failUnless(len(_out_text))
        self.failUnless(len(_err_text))

        self.failUnless('_test42.main.models.Profile' in _out_text)
        self.failUnless('_test42.main.models.RequestLog' in _err_text)

    def test_signals(self):
        rlog = RequestLog.objects.create(method='GET', \
                                 url="/requests/", \
                                 remote_addr="http://localhost/")

        changes_log = ModelChangesLog.objects.filter(name='RequestLog', \
                                 action='create')
        self.failUnless(changes_log)

        rlog.remote_addr = 'http://localhost:8080/'
        rlog.save()

        changes_log = ModelChangesLog.objects.filter(name='RequestLog', \
                                 action='edit')
        self.failUnless(changes_log)

        rlog.delete()
        changes_log = ModelChangesLog.objects.filter(name='RequestLog', \
                                 action='delete')
        self.failUnless(changes_log)
