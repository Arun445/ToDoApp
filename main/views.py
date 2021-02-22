from django.shortcuts import render, redirect, reverse
from .models import ToDoApp, ToDos
from django.utils import timezone
from .forms import TodoForm
#-----------Register--------
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required




@login_required
def base(request):
    logged_users_name = request.user.username
    logged_user = ToDoApp.objects.get(name=logged_users_name)
    logged_user_id = logged_user.id
    context ={
        'user_id':logged_user_id
    }
    return render(request, 'main/base.html', context)


@login_required
def home(request, id):
    logged_users_name = request.user.username
    logged_user = ToDoApp.objects.get(pk=id)
    logged_user_id = ToDoApp.objects.get(name=logged_users_name).id

    if logged_users_name == logged_user.name:

        not_completed_todos = logged_user.todos_set.filter(todo_completed=False)
        try:
            first_todo = not_completed_todos[0]
        except:
            first_todo = 'None'


        context = {
            'all_todos': not_completed_todos,
            'users': logged_user,
            'user_id':logged_user_id,
            'first_todo': first_todo,
        }
    else:
        return redirect('/accounts/sign_up/')

    return render(request, "main/home.html", context )

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            todo = ToDoApp.objects.create(name=username)
            todo.save()
            user = form.save()
            login(request, user)
            return redirect('/')

    context['form']=form
    return render(request,'registration/sign_up.html',context)


@login_required
def create_todo_form(request):
    form = TodoForm(request.POST or None)
    logged_users_name = request.user.username
    logged_user = ToDoApp.objects.get(name=logged_users_name)
    logged_user_id = logged_user.id
    if form.is_valid():
        todo_text = (form.cleaned_data['todo'])
        logged_user = ToDoApp.objects.get(pk=logged_user_id)
        logged_user.todos_set.create(todo=todo_text, todo_completed=False)
        return redirect('/home/%i' %logged_user_id)
    context = {
        'form':form,
        'user_id': logged_user_id,

    }
    return render(request, "main/create.html", context)

@login_required
def update(request, id):
    logged_users_name = request.user.username
    logged_user = ToDoApp.objects.get(name=logged_users_name)
    logged_user_id = logged_user.id
    get_todo = logged_user.todos_set.get(id=id)
    form = TodoForm(request.POST or None, instance=get_todo)
    if form.is_valid():
        form.save()
        return redirect('/home/%i' %logged_user_id )
    context = {
        'form':form,
        'user_id':logged_user_id,
    }
    return render(request, "main/update.html", context)

@login_required
def delete(request, id):
    logged_users_name = request.user.username
    logged_user = ToDoApp.objects.get(name=logged_users_name)
    logged_user_id = logged_user.id
    get_todo = logged_user.todos_set.get(id=id)
    get_todo.delete()

    return redirect("/home/%i" %logged_user_id )

@login_required
def completed(request, id):
    logged_users_name = request.user.username
    logged_user = ToDoApp.objects.get(name=logged_users_name)
    logged_users_id = logged_user.id
    if request.method == 'POST':
        logged_users_todo = logged_user.todos_set.get(id=id)
        logged_users_todo.todo_completed = True
        logged_users_todo.save()
        return redirect("/home/%i" %logged_users_id )
    completed_todos = logged_user.todos_set.filter(todo_completed=True)
    try:
        first_todo = completed_todos[0]
    except:
        first_todo = 'None'
    context = {
        'completed_todos': completed_todos,
        'user_id': logged_users_id,
        'first_todo': first_todo,
    }
    return render(request, 'main/completed.html', context)


