from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    fun_fact = models.CharField(max_length=500, null=True, blank=True)
    profile_picture = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username
