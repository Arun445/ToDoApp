from django.shortcuts import render, redirect
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

def main(request):
    return render(request, 'main/main.html')


def home(request, id):
    name = request.user.username
    user = ToDoApp.objects.get(pk=id)

    if name == user.text:

        all_todos = user.todos_set.all()

        context = {
            'all_todos': all_todos,
            'user': user,
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


def todo_list(request, id):
    user = ToDoApp.objects.get(id=id)
    all_todos = user.todos_set.all()

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
        tod = (form.cleaned_data['todo'])
        name = request.user.username
        idi = ToDoApp.objects.get(text=name)
        idis = idi.id
        q = ToDoApp.objects.get(pk=idis)
        q.todos_set.create(todo=tod)

        return redirect('/home/%i' %idis )
    context = {
        'form':form

    }
    return render(request, "main/create.html", context)


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


def delete(request, id):
    name = request.user.username
    user = ToDoApp.objects.get(text=name)
    user_id = user.id
    get_todos = user.todos_set.get(id=id)
    get_todos.delete()
    #todo = ToDoApp.objects.get(id=id)
    #todo.delete()
    return redirect("/home/%i" %user_id )



'''
def create_todo(request):
    content = (request.POST.get('content', False))
    todo_create = ToDoApp.objects.create(text=content, date=timezone.now())

    context = {
        'create': todo_create,
    }
    return render(request, 'main/create.html', context)
'''


