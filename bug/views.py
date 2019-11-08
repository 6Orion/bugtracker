from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

from .models import Bug
from .forms import BugModelForm

# Constants

# String representation of app's name in lowercase
appname_lower = 'bug'

# String representation of app's name with first letter capitalized 
appname_caps = 'Bug'

# Main model of this app
app_model = Bug

# Main form of this app
app_form = BugModelForm



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
    activities = obj.activities.all()

    template = "detail.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "detail": True, 
                "page_title": f"{appname_caps} ID {id} - Details", 
                "object": obj, 
                # lowercase name of the app to be included as a list
                "list_to_include": "activity/list.html",
                # name/caption of the list
                "list_name": "Activity list",
                # query of child elements
                "query": activities,
                }
    return render(request, template, context)


@login_required
def create(request):
    form = app_form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = app_form
        return redirect("/")

    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "form_custom_template": True,
                "page_title": f"Add new {appname_lower}", 
                "form":form,
                }
    return render(request, template, context)


@login_required
def edit(request, id):
    obj = get_object_or_404(app_model, id = id)
    form = app_form(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/")

    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "custom_form_template": True,
                "page_title": f"{appname_caps} ID {id} - Edit entry", 
                "form": form,
                }
    return render(request, template, context)


@login_required
def delete(request, id):
    obj = get_object_or_404(app_model, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect("/")

    template = f"{appname_lower}/delete.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title": f"{appname_caps} ID {id} - Delete entry", 
                "object":obj,
                }
    return render(request, template, context)

