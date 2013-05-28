# coding=utf-8
import sys

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        for content_type in ContentType.objects.all():
            model = content_type.model_class()

            output = "%s.%s\t%d" % (model.__module__, model.__name__, \
                                    model._default_manager.count())
            print output
            print >> sys.stderr, 'error: %s' % output
