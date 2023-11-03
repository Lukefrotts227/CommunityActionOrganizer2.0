from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class baseUser(AbstractUser):
    
    class Meta:
        app_label = 'my_auth'  # Ensure this is unique
