from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    wallet = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self): 
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
