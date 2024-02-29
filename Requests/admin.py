from django.contrib import admin
from .models import Schedules, AssignedTeams, Request

# Register your models here.


admin.site.register(Schedules)
admin.site.register(AssignedTeams)
admin.site.register(Request)

