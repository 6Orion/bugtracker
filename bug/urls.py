from django.urls import path

from .views import (
    detail,
    create,
    edit,
    delete,
)

from bugtracker.views import (
    home_page,
)

urlpatterns = [
    path("<int:id>/", detail),
    path("<int:id>/edit/", edit),
    path("<int:id>/delete/", delete),

    path("create/", create),
    path("list/", home_page),
] 