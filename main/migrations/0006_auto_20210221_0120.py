# Generated by Django 3.1.6 on 2021-02-21 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_todos_todo_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoapp',
            old_name='text',
            new_name='name',
        ),
    ]
