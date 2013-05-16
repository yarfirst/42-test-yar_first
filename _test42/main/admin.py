# coding=utf-8
from django.contrib import admin


from models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birth_date')
                    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Profile, ProfileAdmin)
