from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(default="title",max_length=50)
    description = models.CharField(default="desc",max_length=50)
    status = models.BooleanField()