from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following_users', blank=True)

    def follow(self, user):
    
        if user != self:
            self.following.add(user)

    def unfollow(self, user):

        if user != self:
            self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(id=user.id).exists()
    
