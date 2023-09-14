from django.shortcuts import render
from django.http import request, HttpResponse
from .models import *
from .forms import *
# Create your views here.
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
