from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q


# Model managers

class ProjectManager(models.Manager):
    def get_queryset(self):
        # Project.objects.all()
        return ProjectQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query == None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


# Query sets

class ProjectQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (Q(name__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(author__first_name__icontains=query) |
                  Q(author__last_name__icontains=query) |
                  Q(author__username__icontains=query))
        return self.filter(lookup)   


# Models
    
class Project(models.Model):
    # fields of the model
    # id = models.IntegerField() # pk
    name         = models.CharField(max_length=70)
    description  = models.TextField()

    author       = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='project_authors')

    created_on   = models.DateTimeField(auto_now_add=True)
    updated_on   = models.DateTimeField(auto_now=True)


    # custom managers
    objects      = ProjectManager()


    # special methods

    def __str__(self):
        return f"{self.name}"


    def get_absolute_url(self):
        return f"/project/{self.id}"


    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    