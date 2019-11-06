from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import RequestContext


# Custom 404 view

def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


# Other views

from bug.models import Bug

def home_page(request):
    query = Bug.objects.all()
    context = {"appname":"bug", "page_title":"Homepage", "query":query,}
    template = "home.html"
    return render(request, template, context)

