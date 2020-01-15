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
from activity.models import Activity

def home_page(request):
    query = Bug.objects.all()

    total_bugs = query.count()
    open_bugs = Bug.objects.open().count()
    closed_bugs = total_bugs - open_bugs
    activities = Activity.objects.all().count()
    percentage_of_open_bugs = "{:2.0f}".format(closed_bugs / total_bugs * 100)
    
    template = "home.html"
    context = {
                "appname_lower": "bug", 
                "appname_caps": "Bug", 
                "page_heading": "Dashboard",
                "page_title": "Bug list", 
                "query": query,
                "total_bugs": total_bugs,
                "open_bugs": open_bugs,
                "close_bugs": closed_bugs,
                "activities": activities,
                "percentage": percentage_of_open_bugs,
                }
    
    return render(request, template, context)

