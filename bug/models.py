from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q

from project.models import Project


# Model managers

class BugManager(models.Manager):
    def get_queryset(self):
        # Bug.objects.all()
        return BugQuerySet(self.model, using=self._db)
    
    def open(self):
        return self.get_queryset().open()

    def search(self, query=None):
        if query == None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)

# Query sets

class BugQuerySet(models.QuerySet):
    def open(self):
        # Bug.objects.all()
        return self.filter(resolution__lte=2)

    def search(self, query):
        lookup = (Q(summary__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(category__icontains=query) |
                  Q(author__first_name__icontains=query) |
                  Q(author__last_name__icontains=query) |
                  Q(author__username__icontains=query))
        return self.filter(lookup)   


# Models

class Bug(models.Model):

    # constants of the model
    
    CATEGORY = [
        ('FRONT', 'Frontend'),
        ('BACK', 'Backend'),
        ('OTHER', 'Other'),
    ]

    VIEW_STATUS = [
        ('1', 'Public'),
        ('0', 'Private'),
    ]

    PRIORITY = [
        ('0', 'None'),
        ('1', 'Low'),
        ('2', 'Normal'),
        ('3', 'High'),
        ('4', 'Urgent'),
        ('5', 'Immediate'),
    ]

    RESOLUTION = [
        ('0', 'Open'),
        ('1', 'Reopened'),
        ('2', 'Unable to reproduce'),
        ('3', 'Closed'),
        ('4', 'Suspended'),
    ]

    SEVERITY = [
        ('0', 'Feature'),
        ('1', 'Trivial'),
        ('2', 'Text'),
        ('3', 'Tweak'),
        ('4', 'Minor'),
        ('5', 'Major'),
        ('6', 'Crash'),
        ('7', 'Block'),
    ]

    # fields of the model
    
    # id = models.IntegerField() # pk
    
    category     = models.CharField(max_length=10, choices=CATEGORY, default='OTHER')
    view_status  = models.CharField(max_length=1, choices=VIEW_STATUS, default='1')
    priority     = models.CharField(max_length=1, choices=PRIORITY, default='0')
    resolution   = models.CharField(max_length=1, choices=RESOLUTION, default='0')
    severity     = models.CharField(max_length=1, choices=SEVERITY, default='0')

    created_on   = models.DateTimeField(auto_now_add=True)
    updated_on   = models.DateTimeField(auto_now=True)

    author       = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='author_of_bugs')
    assigned_to  = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL, related_name="assigned_to_bugs")
    project      = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_bugs")

    summary      = models.CharField(max_length=120)
    description  = models.TextField(null=True, blank=True)
    # image        = models.ImageField(upload_to='image/', blank=True, null=True)

    # custom managers
    
    objects      = BugManager()


    # special methods

    def __str__(self):
        return f"{self.summary}"


    def get_absolute_url(self):
        return f"/bug/{self.id}"


    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit/"
    

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete/"





        