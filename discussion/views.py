from django.shortcuts import render
from django.http import request, HttpResponse
from .models import *
from .forms import *
# Create your views here.

#create 
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

#read
def read_discussion(request):
    contents = Discussion.objects.all()
    return render(request, 'discussion.html', {"content": contents})

#update
def update_discussion(request, pk):
    content = Discussion.objects.get(id = pk)
    discussion_content = request.POST(request, instance = content)
    if discussion_content.is_valid():
        discussion_content.save()
        return render('#')
    return render(request, 'discussion.html')

#delete
def delete_discussion(request, pk):
    content_to_delete = Discussion.objects.get(id = pk)
    content_to_delete.delete()
    return render(request, 'discussion.html')


#read a specific discussion
def read_discussions(request, pk):
    content = Discussion.objects.get(id = pk)
    return render(request, 'discussion-content.html', {"content" : content})