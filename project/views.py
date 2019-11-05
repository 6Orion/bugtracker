from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

from .models import Project
from .forms import ProjectModelForm

# CONSTANTS

appname = "project"

# VIEWS
def project_list(request):
    query = Project.objects.all()
    context = {"appname":appname, "page_title":"Project list", "query": query,}
    template = "home.html"
    return render(request, template, context)

def detail(request, id):
    obj = get_object_or_404(Project, id = id)
    context = {"page_title": f"Details", "detail":True, "object": obj}
    template = "project/detail.html"
    return render(request, template, context)

@login_required
def create(request):
    form = ProjectModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        print(request.user)
        obj.save()
        form = ProjectModelForm
        return redirect("/project/")
    context = {"page_title":"Add new project", "form":form}
    template = "project/form.html"
    return render(request, template, context)

@login_required
def edit(request, id):
    obj = get_object_or_404(Project, id = id)
    form = ProjectModelForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/project/")
    context = {"page_title": f"Edit project", "form":form}
    template = "project/form.html"
    return render(request, template, context)

@login_required
def delete(request, id):
    obj = get_object_or_404(Project, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect("/project/")
    context = {"page_title": f"Delete project", "object":obj}
    template = "project/delete.html"
    return render(request, template, context)