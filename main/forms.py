from django import forms
from .models import ToDoApp, ToDos
from django.contrib.auth.forms import UserCreationForm

class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDos
        fields = ['todo']