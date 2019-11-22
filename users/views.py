from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
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
    obj = get_object_or_404(app_model, id = id)
        
    template = "detail.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "detail": True, 
                "page_title": f"{appname_caps} ID {id} - Details", 
                "object": obj, 
                }
    
    return render(request, template, context)


@login_required
def create(request):
    form = app_create_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = app_create_form
        return redirect("/")

    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "custom_form_template": False,
                "page_title": f"Add new {appname_lower}", 
                "form":form,
                }
    return render(request, template, context)


@login_required
def edit(request, id):
    obj = get_object_or_404(app_model, id = id)
    form = app_edit_form(request.POST or None, request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        print(request.POST)
        return redirect("/")

    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "custom_form_template": False,
                "page_title": f"{appname_caps} ID {id} - Edit entry", 
                "form": form,
                }
    return render(request, template, context)


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(f"{user.get_absolute_url()}")
    else:
        template = "form.html"
        context = {
                    "appname_lower": appname_lower,
                    "appname_caps": appname_caps,
                    "page_title": f"{appname_caps} ID {id} - Edit entry", 
                    "form": form,
                    }
        return render(request, template, context)
        


def logout_view(request):
    logout(request)
    return redirect("/")



