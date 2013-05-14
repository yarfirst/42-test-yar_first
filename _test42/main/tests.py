"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from models import Profile, Contacts


class Test(TestCase):
    
    fixtures = ['profile.json', 'contacts.json']

    def test_profile_exists(self):
        profiles = Profile.objects.all()
        profiles = list(profiles)
        self.failUnless(profiles)
        
        p = profiles[0]
        self.failUnlessEqual(p.name, 'Some name')
        
        contacts = p.contacts_set.all()
        contacts = list(contacts)
        self.failUnless(contacts)
        
        c = contacts[0]
        self.failUnlessEqual(c.jabber, 'some@email.com')
    
    def test_profile_page(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        
        self.failUnless(res.context['profile'])
        
        
        

        
