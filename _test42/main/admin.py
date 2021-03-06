# coding=utf-8
from django.contrib import admin


from models import Profile, RequestLog, ModelChangesLog


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birth_date')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'method', 'url', 'remote_addr', 'order')


class ModelChangesLogAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'name', 'action')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(RequestLog, RequestLogAdmin)
admin.site.register(ModelChangesLog, ModelChangesLogAdmin)
