from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.base, name='base'),
    path('home/<int:id>', views.home, name='home'),
    path('create/', views.create_todo_form, name='create'),
    path('home/<int:id>/update/', views.update, name='update'),
    path('home/<int:id>/delete/', views.delete, name='delete'),
    path('home/<int:id>/completed/', views.completed, name='completed'),
    path('accounts/sign_up/', views.sign_up, name="sign-up"),

]