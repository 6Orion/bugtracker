from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='image/users/', blank=True, null=True)
    

    def __str__(self):
        return self.username


    def get_absolute_url(self):
        return f"/users/{self.id}"

    
    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit/"

    
    def get_edit_password_url(self):
        return f"/users/password/"
    

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete/"


    def get_create_url(self):
        return f"{self.get_absolute_url()}/register/"