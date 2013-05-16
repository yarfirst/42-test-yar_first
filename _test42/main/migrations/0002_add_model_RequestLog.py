# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestLog'
        db.create_table('main_requestlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('remote_addr', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('main', ['RequestLog'])


    def backwards(self, orm):
        # Deleting model 'RequestLog'
        db.delete_table('main_requestlog')


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
        },
        'main.requestlog': {
            'Meta': {'object_name': 'RequestLog'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'remote_addr': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['main']