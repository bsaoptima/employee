from django.contrib import admin
from .models import Consultant, Department, Team, Project, Client

# Register your models here.

admin.site.register(Consultant)
admin.site.register(Department)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Client)