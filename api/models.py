from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(verbose_name='phone', max_length=50)

    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']

    USERNAME_FIELD = 'email'
    def get_username(self):
        return self.email