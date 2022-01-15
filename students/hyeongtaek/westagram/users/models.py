from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32, unique=True)
    email= models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=50)

    class Meta:
        db_table= 'users'






