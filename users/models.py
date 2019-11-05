from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    image       = models.ImageField(upload_to='image/users/', blank=True, null=True)
    
    