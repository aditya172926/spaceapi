from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UserData(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    origin = models.CharField(default='', max_length=50)