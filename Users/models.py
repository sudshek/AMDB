from __future__ import unicode_literals
from django.db import models


# Create your models
class users(models.Model):
    name  = models.CharField(max_length=255, null=False,Blank=False)
    username = models.CharField(max_length=255, null=False, Blank=False)
    email = models.CharField(max_length=255, null=False, Blank=False)
    contact = models.IntegerField(max_length=15)
    password = models.CharField(max_length=255, null=False,Blank=False)
    short_bio = models.CharField(max_length=255, null=False,Blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)