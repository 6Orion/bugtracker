from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

from .models import Bug
from .forms import BugModelForm
from activity.models import Activity

# Create your views here.

def detail(request, id):
    obj = get_object_or_404(Bug, id = id)
    activities = obj.activities.all()
    context = {"page_title": f"Bug ID {id} - Details", "detail":True, "object": obj, "activities":activities}
    template = "bug/detail.html"
    return render(request, template, context)

@login_required
def create(request):
    form = BugModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = BugModelForm
        return redirect("/")
    context = {"page_title":"Add new bug", "form":form}
    template = "bug/form.html"
    return render(request, template, context)

@login_required
def edit(request, id):
    obj = get_object_or_404(Bug, id = id)
    form = BugModelForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {"page_title": f"Bug ID {id} - Edit entry", "form":form}
    template = "bug/form.html"
    return render(request, template, context)

@login_required
def delete(request, id):
    obj = get_object_or_404(Bug, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {"page_title": f"Bug ID {id} - Delete entry", "object":obj}
    template = "bug/delete.html"
    return render(request, template, context)

