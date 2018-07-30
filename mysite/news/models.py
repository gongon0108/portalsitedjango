from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField('Content')
    created_date = models.DateTimeField(
        default=timezone.now)