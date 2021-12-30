from django.db import models
from django.utils import timezone

from django.db.models.deletion import CASCADE


# Create your models here.
class Confession(models.Model):
    user_alias = models.CharField(max_length=15, blank=False)
    confession = models.TextField(max_length=2000, blank=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.user_alias
    

class Comment(models.Model):
    target = models.ForeignKey(Confession, on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=15, blank=False)
    comment_body = models.TextField(max_length=2000, blank=False)
    comment_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)

    def __str__(self):
        return self.commenter_name