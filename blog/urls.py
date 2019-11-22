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
    
    # Design decision: Create view ("create/") has to be parsed before blog post slugs as collision will occur
    path('create/', create),

    path('<str:slug>/', detail),
    path('<str:slug>/edit/', edit),
    path('<str:slug>/delete/', delete),
        
]
