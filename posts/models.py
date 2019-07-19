from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Post(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    desc = models.TextField(max_length=150)
    likes = ArrayField(models.IntegerField(), blank=True, default=list)
    comments = ArrayField(ArrayField(models.CharField(max_length=30), blank=True, default=list), blank=True, default=list)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)





    def __str__(self):
        return self.title


