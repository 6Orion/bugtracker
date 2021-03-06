from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bug
from. serializers import BugSerializer


@api_view(['GET', 'POST'])
def api_list(request):
    """List bugs or create a new bug."""

    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        bugs = Bug.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(bugs, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = BugSerializer(
            data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data,
                         'count': paginator.count,
                         'numpages': paginator.num_pages,
                         'nextlink': '/api/bugs/?page=' + str(nextPage),
                         'prevlink': '/api/bugs/?page=' + str(previousPage),
                         })

    elif request.method == 'POST':
        serializer = BugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, id):
    """Retrieve, update or delete a bug by ID/PK"""

    try:
        bug = Bug.objects.get(id=id)
    except Bug.DoesNotExist:
        return response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BugSerializer(bug, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BugSerializer(bug, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

