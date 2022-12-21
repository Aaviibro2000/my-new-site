from django.db import models 
from django.contrib.auth.admin import User


class Profile(models.Model):
    def __str__(self):
        return self.user.username
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(blank=True,upload_to='profile_pics')
    contact_number=models.CharField(max_length=10)