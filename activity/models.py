from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q

from bug.models import Bug

# Create your models here.

class ActivityManager(models.Manager):
    def get_queryset(self):
        # Activity.objects.all()
        return ActivityQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query == None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)

class ActivityQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (Q(summary__icontains=query) | 
                  Q(content__icontains=query) |
                  Q(bug__summary__icontains=query) |
                  Q(author__first_name__icontains=query) |
                  Q(author__last_name__icontains=query) |
                  Q(author__username__icontains=query))
        return self.filter(lookup) 

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
        return f"{self.get_absolute_url()}/edit/"
    

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete/"