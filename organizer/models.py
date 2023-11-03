from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class baseUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    class Meta:
        app_label = 'my_auth'  # Ensure this is unique
