from django.db import models
from django.conf import settings
from django.utils import timezone

from bug.models import Bug

# Create your models here.

class ActivityManager(models.Manager):
    pass

class ActivityQuerySet(models.QuerySet):
    pass

class Activity(models.Model):

    # fields of the model
    author       = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='activities')
    bug          = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='activities')
    summary      = models.CharField(max_length=120)
    content      = models.TextField(null=True, blank=True)

    created_on   = models.DateTimeField(auto_now_add=True)
    updated_on   = models.DateTimeField(auto_now=True)


    # custom managers
    objects      = ActivityManager()

    # special methods
    def __str__(self):
        return f"{self.bug.project} - {self.bug} - {self.summary}"

    
    def get_absolute_url(self):
        return f"/activity/{self.id}"


    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"