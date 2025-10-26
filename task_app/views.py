# task_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# 一覧表示
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_app/task_list.html', {'tasks': tasks})

# タスク作成
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_app/task_form.html', {'form': form, 'title': '新しいタスクを追加'})

# タスク編集
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_app/task_form.html', {'form': form, 'title': 'タスクを編集'})

# タスク削除
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_app/task_confirm_delete.html', {'task': task})
