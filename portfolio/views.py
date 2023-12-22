from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})


def not_found(request):
    return render(request, 'portfolio/not_found.html')