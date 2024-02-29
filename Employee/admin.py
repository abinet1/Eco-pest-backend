from django.contrib import admin
from .models import EmergencyContact, Employees, Team 

# Register your models here.


admin.site.register(EmergencyContact)
admin.site.register(Employees)
admin.site.register(Team)