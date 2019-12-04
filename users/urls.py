from django.urls import path
from django.contrib.auth import views

from .views import (
    detail,
    create,
    edit,
    edit_password,
    list_view,
    login_view,
    logout_view,
)


urlpatterns = [
    path("", list_view),

    path("<int:id>/", detail),
    path("<int:id>/edit/", edit),

    path("register/", create),

    path('login/', login_view),     
    path('logout/', logout_view),

    path("password/", edit_password),

    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] 