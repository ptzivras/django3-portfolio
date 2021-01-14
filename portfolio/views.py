from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def home(request):
    #return HttpResponse('Personal Portfolio')
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

