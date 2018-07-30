from django.db import models


# Create your models here.
class Calendar(models.Model):
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=40)
    location = models.CharField(max_length=60)