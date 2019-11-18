from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='image/users/', blank=True, null=True)
    
<<<<<<< HEAD

    def __str__(self):
        return self.username


=======
    
>>>>>>> 5278d4fa3b7b1539a89eb2fcc1e0cd3387932f26
    def get_absolute_url(self):
        return f"/users/{self.id}"

    
    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"