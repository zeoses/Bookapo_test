from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    last_activity_time = models.DateTimeField(default=datetime.now)
    
    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ("user",)
