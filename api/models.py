from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UserData(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    origin = models.CharField(default='', max_length=50)
    continent = models.CharField(default='', max_length=50)
    country = models.CharField(default='', max_length=50)