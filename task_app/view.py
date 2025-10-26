from django.shortcuts import render, redirect, get_object_or_404
from .models import Task  # Taskモデルを使う場合

# --- タスク一覧ページ ---
def task_list(request):
    # DBから取得する場合
    tasks = Task.objects.all().order_by('deadline')
    
    # DBをまだ作っていない場合は仮データでテスト
    # tasks = ["勉強", "運動", "読書"]
    
    return render(request, 'task_app/task_list.html', {'tasks': tasks})

# --- タスク追加ページ ---
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        deadline = request.POST['deadline']
        Task.objects.create(title=title, description=description, deadline=deadline)
        return redirect('task_list')
    return render(request, 'task_app/add_task.html')

# --- タスク編集ページ ---
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.deadline = request.POST['deadline']
        task.progress = int(request.POST.get('progress', 0))
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'task_app/edit_task.html', {'task': task})

# --- タスク削除ページ ---
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
