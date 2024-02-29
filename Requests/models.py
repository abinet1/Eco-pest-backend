from django.db import models
from  Employee.models import Employees, Team
from  Clients.models import Clients
from  Store.models import Medicines


# Create your models here.

class Schedules(models.Model):
    date = models.DateField(max_length=30)
    visit_shift = {
        "M": "Morning",
        "A": "Afternoon",
        "N": "Night ",
    }
    time = models.IntegerField()


class AssignedTeams(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    selected_members = models.ManyToManyField(Employees)

class Request(models.Model):
    clients=models.ForeignKey(Clients,on_delete=models.CASCADE)
    Type_of_visit = models.CharField(choices={
        "Major spray application visit": "Major spray application visit ",
        "Minor spray application visit": "Minor spray application visit  ",
        "Major non-spray application visit": "Major non-spray application visit",
        "Minor non-spray application visit": "Minor non-spray application visit",
        "Major pesticide Spray and Rodenticide Treatment": "Major pesticide Spray and Rodenticide Treatment",
        "Major pesticide Non-Spray and Rodenticide Treatment": "Major pesticide Non-Spray and Rodenticide Treatment",
        "Rodent application visit": "Rodent application visit",
        "Room spray treatment": "Room spray treatment",        
        "Room Non-spray treatment": "Room Non-spray treatment",
        "Structural Fumigation": "Structural Fumigation",
        "Furniture Fumigation": "Furniture Fumigation",
        "Inspection for quotation": "Inspection for quotation",
        "Regular follow-up and monitoring ": "Regular follow-up and monitoring",
        "Major spray + Non-spray treatment ": "Major spray + Non-spray treatment",
    }, max_length=200)
    current_condition = models.CharField(max_length=30)
    locatiion_to_be_covered = models.CharField(max_length=60)
    Additional_task = models.CharField(max_length=30)
    detail = models.CharField(max_length=30)
    schedules=models.ForeignKey(Schedules,on_delete=models.CASCADE)
    assigned_teams=models.ForeignKey(AssignedTeams,on_delete=models.CASCADE)
