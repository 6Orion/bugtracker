from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q


# Model managers

class BlogPostManager(models.Manager):
    def get_queryset(self):
        # BlogPost.objects.all()
        return BlogPostQuerySet(self.model, using=self._db)
    
    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query == None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


# Query sets

class BlogPostQuerySet(models.QuerySet):
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


# Models

class BlogPost(models.Model):
    # id = models.IntegerField() # pk
    author       = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, on_delete=models.SET_NULL, related_name="blogposts")
    title        = models.CharField(max_length= 120)
    slug         = models.SlugField(unique=True)
    content      = models.TextField(null=True, blank=True)
    published    = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True )
    timestamp    = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()


    class Meta:
        ordering = ['-pk', '-publish_date', '-updated', '-timestamp']


    # Special methods

    def __str__(self):
        return f"{self.title}"
    
    def get_app_url(self):
        return f"/blog/"

    def get_absolute_url(self):
        return f"{self.get_app_url()}/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    
    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def get_create_url(self):
        return f"{self.get_app_url()}/create"

    def get_list_url(self):
        return {self.get_app_url()}

    
