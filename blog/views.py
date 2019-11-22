from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import BlogPost
from .forms import BlogPostModelForm
# Constants

# String representation of app's name in lowercase
appname_lower = 'blog'

# String representation of app's name with first letter capitalized 
appname_caps = 'Blog'

# Main model of this app
app_model = BlogPost

# Main form of this app
app_form = BlogPostModelForm


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


def detail(request, slug):
    obj = get_object_or_404(app_model, slug = slug)
    template = "detail.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "detail": True,
                "page_title": f"{appname_caps} entry {id}. - {obj.title}",
                "object": obj,
                "child_list": False,
                }

    return render(request, template, context)


@login_required
def create(request):
    form = app_form(request.POST or None, request.FILES or None,)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = app_form
        return redirect(f"/{appname_lower}/{obj.slug}")
    
    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title": f"Add new {appname_lower} entry", 
                "form":form,
                }
    return render(request, template, context)


@login_required
def edit(request, slug):
    obj = get_object_or_404(app_model, slug = slug)
    form = ProjectModelForm(request.POST or None, request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect(f"/{appname_lower}/{obj.slug}")
    
    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "custom_form_template": True,
                "page_title": f"{appname_caps} entry {id}. - {obj.title} - Edit entry", 
                "form":form,
                }
    return render(request, template, context)


@login_required
def delete(request, slug):
    obj = get_object_or_404(app_model, slug = slug)
    if request.method == "POST":
        obj.delete()
        return redirect(f"/{appname_lower}/")

    template = f"{appname_lower}/delete.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title": f"{appname_caps} entry {id}. - {obj.title} - Delete entry", 
                "object":obj,
                }
    return render(request, template, context)