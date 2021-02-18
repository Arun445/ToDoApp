from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main , name='main'),
    path('home/<int:id>', views.home, name='home'),
    path('list/<int:id>', views.todo_list, name='todo_list'),
    path('<int:id>', views.todo_detail, name='todo_detail'),
    path('create/', views.create_todo_form, name='create'),
    path('home/<int:id>/update/', views.update, name='update'),
    path('home/<int:id>/delete/', views.delete, name='delete'),
    path('accounts/sign_up/', views.sign_up, name="sign-up"),

]