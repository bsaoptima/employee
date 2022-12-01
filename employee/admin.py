from django.contrib import admin
from .models import Consultant, Department, Team, Project, Client, User, Task

# Register your models here.

admin.site.register(Consultant)
admin.site.register(Department)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(User)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_name', 'task_project', 'parent_task']
    ordering = ('parent_task',)
    
    class Meta:
        model = Task
        
admin.site.register(Task, TaskAdmin)
