from django.db import models


class product(models.Model):
     def __str__(self):
          return self.name     
     name = models.CharField(max_length=100,unique=True)
     price = models.FloatField()
     description = models.CharField(max_length=200)