import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Confession(models.Model):
    user_alias = models.CharField(max_length=15)
    confession = models.CharField(max_length=2000)



