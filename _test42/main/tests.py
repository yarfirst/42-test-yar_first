"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class Test(TestCase):
    
    fixtures = ['profile.json', 'contacts.json']
    
    def test_profile_page(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
