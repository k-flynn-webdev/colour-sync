# Generated by Django 3.1.4 on 2021-06-13 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='project',
        ),
    ]
