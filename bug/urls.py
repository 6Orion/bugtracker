from django.urls import path

from .views import (
    detail,
    create,
    edit,
    delete,
    list_view,
)


urlpatterns = [
    path("", list_view),

    path("<int:id>/", detail),
    path("<int:id>/edit/", edit),
    path("<int:id>/delete/", delete),

    path("create/", create),    
] 