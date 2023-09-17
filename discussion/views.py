from django.shortcuts import render
from django.http import request, HttpResponse
from .models import *
from .forms import *
# Create your views here.
def discussionList(requests):
    return render(request)


def create_discussion(request):
    content = Form()
    if request.method == 'POST':
        content = Form(request.POST)
        if content.is_valid():
            content.save()
            return render('#')
        else:
            return HttpResponse("Not a valid form")
    return render(request, 'discussion,html', {"content" : content})            


def update_discussion(requests, pk):
    content = Discussion.objects.get(id = pk)
    discussion_content = request.POST(request, instance = content)
    if discussion_content.is_valid():
        discussion_content.save()
        return render('#')
    return render(request)

def delete_discussion(requests):
    return render(request)

