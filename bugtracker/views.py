from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from bug.models import Bug

def home_page(request):
    query = Bug.objects.all()
    context = {"page_title":"Homepage", "buglist":query,}
    template = "home.html"
    return render(request, template, context)
