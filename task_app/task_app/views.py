from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('deadline')
    return render(request, 'task_app/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        deadline = request.POST['deadline']

        Task.objects.create(
            title=title,
            description=description,
            deadline=deadline or None,
            created_at=timezone.now()
        )
        return redirect('task_list')

    return render(request, 'task_app/add_task.html')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.deadline = request.POST['deadline'] or None
        task.save()
        return redirect('task_list')

    return render(request, 'task_app/edit_task.html', {'task': task})
