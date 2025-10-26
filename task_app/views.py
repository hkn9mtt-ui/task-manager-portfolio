from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('deadline')
    return render(request, 'task_app/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        deadline = request.POST['deadline']
        Task.objects.create(title=title, description=description, deadline=deadline)
        return redirect('task_list')
    return render(request, 'task_app/add_task.html')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.deadline = request.POST['deadline']
        task.progress = request.POST.get('progress', 0)
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'task_app/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

