from distutils.command.upload import upload
from tkinter import image_types

from django.db import models


class product(models.Model):
     def __str__(self):
          return self.name     
     name = models.CharField(max_length=100,unique=True)
     price = models.FloatField()
     description = models.CharField(max_length=200)
     details = models.CharField(max_length=2000,blank=True)
     image = models.ImageField(blank=True,upload_to='images')