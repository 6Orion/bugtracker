from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q


# Create your models here.

class BugManager(models.Manager):
    def get_queryset(self):
        # BlogPost.objects.all()
        return BugQuerySet(self.model, using=self._db)
    
    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query == None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

class BugQuerySet(models.QuerySet):
    def published(self):
        # BlogPost.objects.all()
        now = timezone.now()
        return self.filter(publish_date__lte=now, published=True)

    def search(self, query):
        lookup = (Q(title__icontains=query) | 
                  Q(content__icontains=query) |
                  Q(slug__icontains=query) |
                  Q(user__first_name__icontains=query) |
                  Q(user__last_name__icontains=query) |
                  Q(user__username__icontains=query))
        return self.filter(lookup)   

class Bug(models.Model):

    Author = settings.AUTH_USER_MODEL

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
        ('1', 'Fixed'),
        ('2', 'Reopened'),
        ('3', 'Unable to reproduce'),
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
    # project      = models.ForeignKey()
    category     = models.CharField(max_length=10, choices=CATEGORY, default='OTHER')
    view_status  = models.CharField(max_length=1, choices=VIEW_STATUS, default='1')
    priority     = models.CharField(max_length=1, choices=PRIORITY, default='0')
    resolution   = models.CharField(max_length=1, choices=RESOLUTION, default='0')
    severity     = models.CharField(max_length=1, choices=SEVERITY, default='0')

    created_on   = models.DateTimeField(auto_now_add=True)
    updated_on   = models.DateTimeField(auto_now=True)

    author       = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='authors')
    assigned_to  = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="assigned_to")

    summary      = models.CharField(max_length=240)
    description  = models.TextField(null=True, blank=True)
    # image        = models.ImageField(upload_to='image/', blank=True, null=True)

    # custom managers
    
    objects      = BugManager()


    # special methods

    def __str__(self):
        return f"{self.id} - {self.summary}"


    def get_absolute_url(self):
        return f"/bug/{self.id}"


    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"





        