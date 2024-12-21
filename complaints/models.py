from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone=models.CharField(max_length=100,unique=True)

class Road(models.Model):
    vehicle=models.CharField(max_length=100)
    uploaded_date=models.DateTimeField(auto_now=True)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
     return self.vehicle