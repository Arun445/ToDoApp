from django import forms
from .models import ToDoApp


class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDoApp
        fields = ['text']