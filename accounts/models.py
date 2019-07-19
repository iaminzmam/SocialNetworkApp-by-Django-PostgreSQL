from django.db import models
from django.conf import settings

# Create your models here.

class plans(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comm = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
