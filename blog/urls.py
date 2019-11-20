from django.urls import path

from .views import (
    detail,
    list_view,
    create,
    edit,
    delete,    
)

urlpatterns = [
    path('', list_view),
    
    path('<str:slug>/', detail),
    path('<str:slug>/edit/', edit),
    path('<str:slug>/delete/', delete),

    path('create/', create),
]
