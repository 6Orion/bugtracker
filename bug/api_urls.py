from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .api_views import (
    api_list,
    api_detail,
)

urlpatterns = [
    path("", api_list),
    path("<int:id>/", api_detail),
]