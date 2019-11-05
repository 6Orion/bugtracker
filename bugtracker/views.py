from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from bug.models import Bug

def home_page(request):
    query = Bug.objects.all()
    context = {"appname":"bug", "page_title":"Homepage", "query":query,}
    template = "home.html"
    return render(request, template, context)
