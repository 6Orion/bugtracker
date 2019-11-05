from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

from .models import Activity
from .forms import ActivityModelForm
from bug.models import Bug

# Create your views here.

@login_required
def create(request, bug_id):
    bug = get_object_or_404(Bug, id = bug_id)
    form = ActivityModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.bug = bug
        obj.save()
        return redirect(f"/bug/{bug_id}")
    context = {"page_title":f"Add new activity for bug {bug_id}", "form":form, "bug_id":bug_id}
    template = "activity/form.html"
    return render(request, template, context)


