from django.shortcuts import render

from bug.models import Bug
from project.models import Project
from activity.models import Activity

from .models import SearchQuery

# Create your views here.
def results(request):
    query    = request.GET.get("q", None)
    user     = None

    if request.user.is_authenticated:
        user = request.user

    template = 'search/results.html'
    context = {
                'query': query,
                'page_title': "No search results",
                }

    if query is not None and query != "":
        SearchQuery.objects.create(user=user, query=query)
        project_list = Project.objects.search(query=query)
        bug_list = Bug.objects.search(query=query)
        activity_list = Activity.objects.search(query=query)
        
        context['project_list'] = project_list
        context['bug_list'] = bug_list
        context['activity_list'] = activity_list
        context['page_title'] = f"You searched for {query}"
        
    return render(request, template, context)