from django.contrib import admin
from .models import UserData
# Register your models here.

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    fields = ('author', 'origin')
    list_display = ['author', 'origin']
    search_fields = ('author', 'origin')