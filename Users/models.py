from __future__ import unicode_literals
from django.db import models


# Create your models
class users(models.Model):
    name  = models.CharField(max_length=255, null=False, blank=False)
    username = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    contact = models.IntegerField(default=0)
    password = models.CharField(max_length=255, null=False,blank=False)
    short_bio = models.CharField(max_length=255, null=False,blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)