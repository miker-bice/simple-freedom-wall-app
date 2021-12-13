from django.db import models
from datetime import datetime, date


# Create your models here.
class Confession(models.Model):
    user_alias = models.CharField(max_length=15)
    confession = models.CharField(max_length=2000)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    

