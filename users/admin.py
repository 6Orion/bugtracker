from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form     = CustomUserCreationForm
    form         = CustomUserChangeForm
    model        = CustomUser
    list_display = ['username', 'email', 'is_staff', ]
    
    # Extends default fields list of the UserAdmin form
    # Add additional fields in a following format Tuple(Tuple(strGroupName, dict{'fields': tuple(fieldNames, )}), )
    fieldsets    = UserAdmin.fieldsets + (('Image', {'fields': ('image', )}), )
    
admin.site.register(CustomUser, CustomUserAdmin)
