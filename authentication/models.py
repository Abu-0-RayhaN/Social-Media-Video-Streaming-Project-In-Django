from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='media/profile_pics', blank=True)
    description = models.TextField(blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    
    

