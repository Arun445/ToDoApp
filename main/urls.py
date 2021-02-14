from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:id>', views.todo_detail, name='todo_detail'),
    path('create/', views.create_todo_form, name='create'),
    path('<int:id>/update/', views.update, name='update')

]