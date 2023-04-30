from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Task
from .forms import TaskForm


# from django.urls import reverse
# Create your views here.


# create a task
def task_create(request):
    # 如果用户通过POST提交，通过request.POST获取提交数据
    if request.method == "POST":
        # 将用户提交数据与TaskForm表单绑定
        form = TaskForm(request.POST)
        # 表单验证，如果表单有效，将数据存入数据库
        if form.is_valid():
            form.save()
            # 跳转到任务清单
            return redirect(reverse("tasks:task_list"))
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})


# retrieve task list
def task_list(request):
    # 从数据库获取任务清单
    tasks = Task.objects.all()
    # 指定渲染模板并传递数据
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# retrieve single task list
def task_detail(request, pk):
    # task = Task.objects.filter(id=pk)
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task, })


# update a task
def task_update(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象实例
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_detail", args=[pk, ]))
    else:
        form = TaskForm(instance=task_obj)
    return render(request, "tasks/task_form.html", {"form": form, "object": task_obj})


# Delete a single task
def task_delete(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete()
    # 删除然后跳转
    return redirect(reverse("tasks:task_list"))
