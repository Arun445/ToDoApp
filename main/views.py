from django.shortcuts import render, redirect
from .models import ToDoApp
from django.utils import timezone
from .forms import TodoForm

#-----------CRUD----------


def base(request):
    return render(request, "main/base.html",)

def todo_list(request):
    all_todos = ToDoApp.objects.all()
    context = {
        'all_todos': all_todos
    }
    return render(request, 'main/list.html', context)

def todo_detail(request, id):
    get_todos = ToDoApp.objects.get(id=id)
    context = {
        'get_todos': get_todos,
    }
    return render(request, 'main/detail.html', context)

def create_todo_form(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form':form

    }
    return render(request, "main/create.html", context)


def update(request, id):
    get_todos = ToDoApp.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=get_todos)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form':form
    }
    return render(request, "main/update.html", context)
'''
def create_todo(request):
    content = (request.POST.get('content', False))
    todo_create = ToDoApp.objects.create(text=content, date=timezone.now())

    context = {
        'create': todo_create,
    }
    return render(request, 'main/create.html', context)
'''


