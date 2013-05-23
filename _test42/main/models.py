# coding=utf-8
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


def _log_action(model_name, action):
    changes_log = ModelChangesLog(name=model_name, action=action)
    changes_log.save()
     
    return changes_log
     
 
@receiver(post_save)
def model_post_save(sender, instance, created, **kwargs):
    model_name = sender.__name__
    if model_name != 'ModelChangesLog':
        action = 'create' if created else 'edit'
 
        _log_action(model_name, action)
 
 
@receiver(post_delete)
def model_post_delete(sender, instance, **kwargs):
    model_name = sender.__name__
    if model_name != 'ModelChangesLog':
         
        _log_action(model_name, 'delete')


class Profile(models.Model):

    name = models.CharField('Name', max_length=256)
    surname = models.CharField('Surname', max_length=256)
    birth_date = models.DateField('Date of birth')
    bio = models.TextField('Bio')

    email = models.EmailField()
    jabber = models.CharField(max_length=256)
    skype = models.IntegerField()
    other = models.TextField()

    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    
    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)


class RequestLog(models.Model):

    method = models.CharField(max_length=40)
    url = models.CharField(max_length=256)
    remote_addr = models.CharField(max_length=60)
    datetime = models.DateTimeField(auto_now=True, auto_now_add=True)

    order = models.IntegerField(default=0)


class ModelChangesLog(models.Model):
    
    name = models.CharField(max_length=100)
    action = models.CharField(max_length=40)
    datetime = models.DateTimeField(auto_now=True, auto_now_add=True)
