from django.db import models


# Create your models here.
class Confessions(models.Model):
    user_alias = models.CharField(max_length=15)
    confession = models.CharField(max_length=2000)

