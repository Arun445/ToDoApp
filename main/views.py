from django.shortcuts import render, redirect, reverse
from .models import ToDoApp, ToDos
from django.utils import timezone
from .forms import TodoForm
#-----------Register--------
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

#-----------CRUD----------

#---------------register stuff-------

@login_required
def base(request):
    account_name = request.user.username
    users = ToDoApp.objects.get(text=account_name)
    user_id = users.id
    context ={
        'user_id':user_id
    }
    return render(request, 'main/base.html', context)

@login_required
def main(request):
    return render(request, 'main/main.html')

@login_required
def home(request, id):
    name = request.user.username
    user = ToDoApp.objects.get(pk=id)
    user_id = ToDoApp.objects.get(text=name).id

    if name == user.text:

        all_todos = user.todos_set.filter(todo_completed=False)

        context = {
            'all_todos': all_todos,
            'users': user,
            'user_id':user_id,
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
            todo = ToDoApp.objects.create(text=username)
            todo.save()
            user = form.save()
            login(request, user)
            return redirect('/')

    context['form']=form
    return render(request,'registration/sign_up.html',context)








#-----------------end-------------

#def base(request):
#    return render(request, "main/base.html",)

@login_required
def todo_list(request, id):
    user = ToDoApp.objects.get(id=id)
    all_todos = user.todos_set.all()

    context = {
        'all_todos': all_todos
    }
    return render(request, 'main/list.html', context)

@login_required
def todo_detail(request, id):
    get_todos = ToDoApp.objects.get(id=id)

    context = {
        'get_todos': get_todos,
    }
    return render(request, 'main/detail.html', context)

@login_required
def create_todo_form(request):
    form = TodoForm(request.POST or None)
    name = request.user.username
    idi = ToDoApp.objects.get(text=name)
    user_id = idi.id
    if form.is_valid():
        tod = (form.cleaned_data['todo'])
        #name = request.user.username
        #idi = ToDoApp.objects.get(text=name)
        #user_id = idi.id
        q = ToDoApp.objects.get(pk=user_id)
        q.todos_set.create(todo=tod, todo_completed=False)
        return redirect('/home/%i' %user_id)
    context = {
        'form':form,
        'user_id': user_id,

    }
    return render(request, "main/create.html", context)

@login_required
def update(request, id):
    name = request.user.username
    user = ToDoApp.objects.get(text=name)
    user_id = user.id
#    user = ToDoApp.objects.get(id=idis)
    get_todos = user.todos_set.get(id=id)
    form = TodoForm(request.POST or None, instance=get_todos)
    if form.is_valid():
        form.save()
        return redirect('/home/%i' %user_id )
    context = {
        'form':form
    }
    return render(request, "main/update.html", context)

@login_required
def delete(request, id):
    name = request.user.username
    user = ToDoApp.objects.get(text=name)
    user_id = user.id
    get_todos = user.todos_set.get(id=id)
    get_todos.delete()

    return redirect("/home/%i" %user_id )

def completed(request, id):
    logged_users_name = request.user.username
    logged_user = ToDoApp.objects.get(text=logged_users_name)
    if request.method == 'POST':
        logged_users_id = logged_user.id
        logged_users_todo = logged_user.todos_set.get(id=id)
        logged_users_todo.todo_completed = True
        logged_users_todo.save()
        return redirect("/home/%i" %logged_users_id )
    completed_todos = logged_user.todos_set.filter(todo_completed=True)
    context = {
        'completed_todos': completed_todos

    }
    return render(request, 'main/completed.html', context)


'''
def create_todo(request):
    content = (request.POST.get('content', False))
    todo_create = ToDoApp.objects.create(text=content, date=timezone.now())

    context = {
        'create': todo_create,
    }
    return render(request, 'main/create.html', context)
'''


