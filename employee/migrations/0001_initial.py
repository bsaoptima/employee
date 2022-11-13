# Generated by Django 4.1.2 on 2022-11-13 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_primary_contact', models.CharField(max_length=100)),
                ('client_number_of_projects', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.TextField(max_length=200)),
                ('project_startDate', models.DateTimeField(auto_now_add=True)),
                ('project_endDate', models.DateTimeField(auto_now=True)),
                ('project_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.client')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('isemailvalid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('team_project', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.project')),
            ],
        ),
        migrations.CreateModel(
            name='SignUpToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('code', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.user')),
            ],
        ),
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.department')),
                ('team', models.ForeignKey(default='Unassigned', null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.user')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.user'),
        ),
    ]
