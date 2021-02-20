from django.db import models
from django.utils import timezone


class ToDoApp(models.Model):
    text = models.CharField(max_length=100)


    def __str__(self):
        return self.text

class ToDos(models.Model):
    todolist = models.ForeignKey(ToDoApp, on_delete=models.CASCADE)
    todo = models.CharField(max_length=300)
    todo_completed = models.BooleanField(null=True)

    def __str__(self):
        return self.todo