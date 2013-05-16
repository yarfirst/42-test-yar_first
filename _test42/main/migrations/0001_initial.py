# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Profile'
        db.create_table('main_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('skype', self.gf('django.db.models.fields.IntegerField')()),
            ('other', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['Profile'])


    def backwards(self, orm):
        
        # Deleting model 'Profile'
        db.delete_table('main_profile')


    models = {
        'main.profile': {
            'Meta': {'object_name': 'Profile'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.IntegerField', [], {}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['main']
