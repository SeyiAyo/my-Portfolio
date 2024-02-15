from django.shortcuts import render
from .models import about, project, contact


def index(request):
    about_me = about.objects.all()
    projects = project.objects.all()
    
    context = {
        'about_me': about_me,
        'projects': projects
    }
    return render(request, 'showcase.html', {'about_me' : about_me, 'projects' : projects})