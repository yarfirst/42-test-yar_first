# coding=utf-8
from django.db import models


class Profile(models.Model):

    name = models.CharField('Name', max_length=256)
    surname = models.CharField('Surname', max_length=256)
    birth_date = models.DateField('Date of birth')
    bio = models.TextField('Bio')

    email = models.EmailField()
    jabber = models.CharField(max_length=256)
    skype = models.IntegerField()
    other = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)


class RequestLog(models.Model):

    method = models.CharField(max_length=40)
    url = models.CharField(max_length=256)
    remote_addr = models.CharField(max_length=60)
    datetime = models.DateTimeField(auto_now=True, auto_now_add=True)
