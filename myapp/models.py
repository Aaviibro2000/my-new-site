from django.db import models
from django.contrib.auth.models import User


class product(models.Model):
     def __str__(self):
          return self.name     
     name = models.CharField(max_length=100,unique=True)
     price = models.FloatField()
     description = models.CharField(max_length=200)
     details = models.CharField(max_length=2000,blank=True)
     image = models.ImageField(blank=True,upload_to='images')
     seller = models.ForeignKey(User,on_delete=models.CASCADE)