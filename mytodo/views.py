from django.shortcuts import render
from .models import Task

def home(request):
    context = {
        'tasks': Task.objects.all().order_by('-created_at'),
        'title': 'My To-Do List',
    }
    return render(request, 'mytodo/home.html', context)

