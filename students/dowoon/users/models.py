from django.db import models

class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
