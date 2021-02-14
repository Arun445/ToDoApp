from django.db import models
from django.utils import timezone


class ToDoApp(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.text