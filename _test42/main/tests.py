# coding=utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import sys
from StringIO import StringIO
from urlparse import urlparse

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.management import call_command
from django.core.urlresolvers import reverse
from django.template import Template, context
from django.test import TestCase

from models import Profile, RequestLog, ModelChangesLog


class Test(TestCase):

    def test_profile_exists(self):
        profiles = Profile.objects.all()
        profiles = list(profiles)
        self.assertTrue(profiles)

        p = profiles[0]
        self.assertEqual(p.name, 'Some name')

    def test_profile_page(self):
        res = self.client.get(reverse('profile'))
        self.assertEqual(res.status_code, 200)

        self.assertTrue(res.context['profile'])

        p = Profile.objects.all()[0]
        self.assertContains(res, p.name)
        self.assertContains(res, 'edit_in_admin')

    def test_edit_tag_link(self):
        p = Profile.objects.all()[0]
        tpl = Template('{% load edit_link %}{% edit_link profile %}')
        res = tpl.render(context.Context({'profile': p}))
        self.assertTrue('edit_in_admin' in res)

    def test_request_middleware(self):
        res = self.client.get(reverse('request_log'))
        self.assertEqual(res.status_code, 200)

        request_logs = RequestLog.objects.all().order_by('id')
        self.assertTrue(request_logs)

        self.assertTrue(res.context['request_logs'])

        context_request_logs = res.context['request_logs']

        log_length = len(context_request_logs)
        self.assertTrue(log_length)
        self.assertFalse(log_length > 10)

        self.assertContains(res, '/requests/')

    def test_context_processor(self):
        res = self.client.get(reverse('profile'))
        self.assertEqual(res.status_code, 200)

        self.assertTrue(res.context['SETTINGS'])

    def test_edit_page(self):
        profile = Profile.objects.all()[0]

        profile_edit_url = reverse('profile_edit', \
                                   kwargs={'profile_id': profile.id})

        res = self.client.get(profile_edit_url)
        # self.assertEqual(res.status_code, 302)
        # на мой взгляд предыдущщий вариант прощще
        next_url = REDIRECT_FIELD_NAME + '=' + urlparse(profile_edit_url).path
        dest_url = reverse('login_page')
        dest_url = dest_url + '?' + next_url

        self.assertRedirects(res, dest_url)

        self.client.login(username='admin', password='admin')
        res = self.client.get(profile_edit_url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'id_name')

        data = profile.__dict__
        data['name'] = 'TEST NAME'
        res = self.client.post(profile_edit_url, data)
        # self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, profile_edit_url)

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

        self.assertTrue(len(_out_text))
        self.assertTrue(len(_err_text))

        self.assertTrue('_test42.main.models.Profile' in _out_text)
        self.assertTrue('_test42.main.models.RequestLog' in _err_text)

    def test_signals(self):
        rlog = RequestLog.objects.create(method='GET', \
                                 url="/requests/", \
                                 remote_addr="http://localhost/")

        changes_log = ModelChangesLog.objects.filter(name='RequestLog', \
                                 action='create')
        self.assertTrue(changes_log)

        rlog.remote_addr = 'http://localhost:8080/'
        rlog.save()

        changes_log = ModelChangesLog.objects.filter(name='RequestLog', \
                                 action='edit')
        self.assertTrue(changes_log)

        rlog.delete()
        changes_log = ModelChangesLog.objects.filter(name='RequestLog', \
                                 action='delete')
        self.assertTrue(changes_log)

    def test_delete_request_log(self):
        del_url = reverse('request_log_delete')
        res = self.client.get(del_url)
        self.assertEqual(res.status_code, 404)

        rlog = RequestLog.objects.create(method='GET', \
                                 url="/requests/", \
                                 remote_addr="http://localhost/")

        res = self.client.post(del_url, {'entry_id': rlog.id})
        self.assertEqual(res.status_code, 200)

        requests = RequestLog.objects.filter(id=rlog.id)
        self.assertFalse(requests)
