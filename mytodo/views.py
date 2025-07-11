from django.shortcuts import render
from .models import Task
from django.shortcuts import redirect, get_object_or_404

def home(request):
    context = {
        'tasks': Task.objects.all().order_by('-created_at'),
        'title': 'My To-Do List',
    }
    return render(request, 'mytodo/home.html', context)

def mark_completed(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.completed = True
        task.save()
    return redirect('mytodo_home')  

def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect('mytodo_home')

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Task.objects.create(title=title, description=description, user=request.user)
    return redirect('mytodo_home')                                                                                                  