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
             #   "js_var": [0, 1, 2, 3, 4, 3, 5, 7, 10, 4, 2],
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
                "child_list_planned": False,
                }

    list_query = obj.activities.all()
    
    if list_query.count() != 0:
        context['child_list'] = {
                                # Lowercase name of the app to be included as a list
                                "template": "activity/list.html",
                                # Name/caption of the list
                                "name": "Activity list",
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
        obj.save()
        form = app_form
        return redirect("/")

    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "custom_form_template": True,
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



def search(request):
    q = request.GET.get("q", None)
    
    if q is not None:
        query = Bug.objects.search(query=q)
    else:
        query = None

    template = "list.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title": f"{appname_caps} list",
                "main_content": True,
                "query": query
                }
    return render(request, template, context)

