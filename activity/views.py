from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

from .models import Activity
from .forms import ActivityModelForm
from bug.models import Bug


# Constants

# String representation of app's name in lowercase
appname_lower = 'activity'

# String representation of app's name with first letter capitalized 
appname_caps = 'Activity'

# Main model of this app
app_model = Activity

# Main form of this app
app_form = ActivityModelForm



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
                "page_title": f"{appname_caps} ID {id} - Details",
                "object": obj,

                }
    return render(request, template, context)


@login_required
def create(request, bug_id):
    bug = get_object_or_404(Bug, id = bug_id)
    form = app_form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.bug = bug
        obj.save()
        return redirect(f"/bug/{bug_id}")

    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title":f"Add new activity for bug {bug_id}", 
                "form":form, 
                "bug_id":bug_id,
                }
    return render(request, template, context)


@login_required
def edit(request, id):
    obj = get_object_or_404(app_model, id = id)
    form = app_form(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect(f"/bug/{obj.bug.id}")
    
    template = "form.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title": f"{appname_caps} ID {id} - Edit entry", 
                "form": form,
                }
    return render(request, template, context)


@login_required
def delete(request, id):
    obj = get_object_or_404(app_model, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect(f"/{appname_lower}/{obj.bug.id}")
    
    template = f"{appname_lower}/delete.html"
    context = {
                "appname_lower": appname_lower,
                "appname_caps": appname_caps,
                "page_title": f"{appname_caps} ID {id} - Delete entry", 
                "object":obj,
                }
    return render(request, template, context)
    


