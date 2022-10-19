from django.db import models


class product(models.Model):
     def __str__(self):
          return self.name     
     name = models.CharField(max_length=100)
     price = models.FloatField()
     description = models.CharField(max_length=200)