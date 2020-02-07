from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

class DataInfo(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    url = models.CharField(max_length=255)
    source_website = models.CharField(max_length=255)
