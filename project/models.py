from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.
    
class Project(models.Model):


    #
    # fields of the model
    #

    # id = models.IntegerField() # pk
    name         = models.CharField(max_length=70)
    description  = models.TextField()

    author       = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='project_authors')

    created_on   = models.DateTimeField(auto_now_add=True)
    updated_on   = models.DateTimeField(auto_now=True)



    #
    # custom managers
    #


    # objects      = ProjectManager()


    #
    # special methods
    #

    def __str__(self):
        return f"{self.name}"


    def get_absolute_url(self):
        return f"/project/{self.id}"


    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"