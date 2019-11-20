from django.urls import path
from django.contrib.auth import views

from .views import (
    detail,
    create,
    edit,
    list_view,
    login_view,
    logout_view,
)


urlpatterns = [
    path("", list_view),

    path("<int:id>/", detail),
    path("<int:id>/edit/", edit),

    path("create/", create),

    path('login/', login_view),     
    path('logout/', logout_view),
] 