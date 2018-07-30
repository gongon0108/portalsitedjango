from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField('Content')