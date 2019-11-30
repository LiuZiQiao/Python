from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=32)
    upasswd = models.CharField(max_length=32)


# class Movies(models.Model):
