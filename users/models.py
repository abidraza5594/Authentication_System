from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=20)
    user_image=models.ImageField(default='proflepicture.jpg',upload_to='userpictures.jpg')
    user_location=models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
    
