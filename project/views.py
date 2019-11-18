from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Project
from .forms import ProjectModelForm
# Constants

# String representation of app's name in lowercase
appname_lower = 'project'

# String representation of app's name with first letter capitalized 
appname_caps = 'Project'

# Main model of this app
app_model = Project

# Main form of this app
app_form = ProjectModelForm


# VIEWS
def list_view(request):
    query = app_model.objects.all()

    template = "list.html"    
    context = { 
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title": f"{appname_caps} list",
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
                "child_list": False,
                }
    
    list_query = obj.project_bugs.all()

    if list_query.count() != 0:
        context['child_list'] = {
                                # Lowercase name of the app to be included as a list
                                "template": "bug/list.html",
                                # Name/caption of the list
                                "name": "Bug list",
                                # Query of child elements
                                "query": list_query,
                                }
    return render(request, template, context)


@login_required
def create(request):
    form = app_form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        print(request.user)
        obj.save()
        form = app_form
        return redirect(f"/{appname_lower}/")
    
    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title": f"Add new {appname_lower}", 
                "form":form,
                }
    return render(request, template, context)


@login_required
def edit(request, id):
    obj = get_object_or_404(app_model, id = id)
    form = ProjectModelForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect(f"/{appname_lower}/")
    
    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "custom_form_template": True,
                "page_title": f"{appname_caps} ID {id} - Edit entry", 
                "form":form,
                }
    return render(request, template, context)


@login_required
def delete(request, id):
    obj = get_object_or_404(app_model, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect(f"/{appname_lower}/")

    template = f"{appname_lower}/delete.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title": f"{appname_caps} ID {id} - Delete entry", 
                "object":obj,
                }
    return render(request, template, context)