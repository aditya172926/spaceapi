from django.contrib import admin
from .models import UserData
# Register your models here.

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    fields = ('author', 'origin', 'continent', 'country')
    list_display = ['author', 'origin', 'continent', 'country']
    search_fields = ('author', 'origin', 'continent', 'country')