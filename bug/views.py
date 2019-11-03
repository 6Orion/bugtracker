from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

from .models import Bug
from .forms import BugModelForm

# Create your views here.

def detail(request, id):
    bug = get_object_or_404(Bug, id = id)
    
    context = {"page_title": f"Bug No. {id} - Details", "object": bug}
    template = "bug/detail.html"
    return render(request, template, context)

@login_required
def create(request):
    form = BugModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        print(request.user)
        obj.save()
        form = BugModelForm
        return redirect("/")
    context = {"page_title":"Create a bug", "form":form}
    template = "bug/create.html"
    return render(request, template, context)

def edit(request, id):
    context = {"page_title": f"Bug No. {id} - Edit entry"}
    template = "bug/edit.html"
    return render(request, template, context)

def delete(request, id):
    context = {"page_title": f"Bug No. {id} - Delete entry",}
    template = "bug/delete.html"
    return render(request, template, context)

