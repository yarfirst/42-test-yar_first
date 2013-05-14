# coding=utf-8
from django.db import models


class Profile(models.Model):

    name = models.CharField('Name', max_length=256)
    surname = models.CharField('Surname', max_length=256)

    birth_date = models.DateField('Date of birth')
    bio = models.TextField('Bio')


class Contacts(models.Model):
    profile = models.ForeignKey(Profile)
    
    email = models.EmailField()
    jabber = models.CharField(max_length=256)
    skype = models.IntegerField()

    other = models.TextField()
