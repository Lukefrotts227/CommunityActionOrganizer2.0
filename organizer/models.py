from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager): 
    def create_user(self, email, first_name, last_name, town, password=None): 
        if not email: 
            raise ValueError('Users must have an email')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name=last_name,
            town=town,
        ) 
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self, email, first_name, last_name, town, password=None): 
        user = self.create_user(email, password=password, first_name=first_name, last_name=last_name, town=town)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self.db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    town = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'town']

    def __str__(self): 
        return f'{self.first_name} {self.last_name}'
    def get_email(self): 
        return self.email
    def get_short_name(self):
        return f'{self.first_name} {self.last_name[0]}.'
    def get_shorter_name(self):
        return self.first_name





