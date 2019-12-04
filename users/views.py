from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

from bug.models import Bug
from activity.models import Activity
from project.models import Project


# Constants

# String representation of app's name in lowercase
appname_lower = 'users'

# String representation of app's name with first letter capitalized
appname_caps = 'Users'

# Main model of this app
app_model = CustomUser

# Main forms of this app
app_create_form = CustomUserCreationForm
app_edit_form = CustomUserChangeForm


# Create your views here.
def list_view(request):
    query = app_model.objects.all()

    template = "list.html"
    context = {
        "appname_lower": appname_lower,
        "appname_caps": appname_caps,
        "page_title": f"{appname_caps} list",
        "main_content": True,
        "query": query,
    }
    return render(request, template, context)


def detail(request, id):
    obj = get_object_or_404(app_model, id=id)

    template = "detail.html"
    context = {
        "appname_lower": appname_lower,
        "appname_caps": appname_caps,
        "detail": True,
        "page_title": f"{appname_caps} ID {id} - Details",
        "object": obj,
    }

    return render(request, template, context)


def create(request):
    form = app_create_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect("/")

    template = "users/register.html"
    context = {
        "appname_lower": appname_lower,
        "appname_caps": appname_caps,
        "custom_form_template": False,
        "page_title": f"Add new {appname_lower}",
        "form": form,
    }
    return render(request, template, context)


@login_required
def edit(request, id):
    obj = get_object_or_404(app_model, id=id)
    form = app_edit_form(request.POST or None,
                         request.FILES or None, instance=obj)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            print(request.POST)
            messages.success(request, 'Your profile was successfully updated!')
            return redirect(f"{obj.get_absolute_url()}")
        else:
            messages.error(request, 'Please correct the errors below.', extra_tags="danger")
    
    template = "form.html"
    context = {
        "appname_lower": appname_lower,
        "appname_caps": appname_caps,
        "custom_form_template": False,
        "page_title": f"{appname_caps} ID {id} - Edit entry",
        "form": form,
    }
    return render(request, template, context)


@login_required
def edit_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(f"{request.user.get_absolute_url()}")
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)

    template = "users/edit_password_form.html"
    context = {
        "appname_lower": appname_lower,
        "appname_caps": appname_caps,
        "page_title": f"Change your password",
        "form": form,
    }
    return render(request, template, context)


def login_view(request):
    if request.method != "POST":
        template = "users/login.html"
        context = {
            "appname_lower": appname_lower,
            "appname_caps": appname_caps,
            "page_title": f"Log in to the dashboard",
        }
        return render(request, template, context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f"{user.get_absolute_url()}")
        else:
            template = "users/login.html"
            context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title": f"Log in to the dashboard",
                "error": "Wrong credentials. Please try again.",
                "username": request.POST['username']
            }
            return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect("/")
