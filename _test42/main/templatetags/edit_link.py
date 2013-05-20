from django import template
from django.db.models import Model
from django.contrib import admin
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def edit_link(obj):
    if not isinstance(obj, Model):
        return ''
    
    if obj._meta.concrete_model not in admin.site._registry:
        return ''
    
    url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.module_name), args=[obj.id])
    return u'(<a class="edit_in_admin" href="%s">Edit</a>)' % url
