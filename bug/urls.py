from django.urls import path

from .views import (
    detail,
    create,
    edit,
    delete,
)

urlpatterns = [
    path("<int:id>/", detail),
    path("<int:id>/edit/", edit),
    path("<int:id>/delete/", delete),

    path("create/", create),
] 