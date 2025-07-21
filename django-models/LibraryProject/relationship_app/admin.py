from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ['user__username', 'role']

admin.site.register(UserProfile, UserProfileAdmin)
