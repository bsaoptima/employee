# Generated by Django 4.1.2 on 2022-12-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_task_parent_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_consultant',
            field=models.BooleanField(default=False),
        ),
    ]