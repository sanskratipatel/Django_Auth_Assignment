from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone
class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile') 
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # date_joined = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
