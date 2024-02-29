from django.db import models

# Create your models here.
class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    physical_address = models.CharField(max_length=30)
    work_place = models.CharField(max_length=100)

class Employees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    physical_address = models.CharField(max_length=30)
    date_of_birth = models.DateField(max_length=130)
    emergency_contact =models.ForeignKey(EmergencyContact,on_delete=models.CASCADE)

    Role =models.CharField(choices={
        "CEO": "CEO",
        "CRDO": "CRDO",
        "CRO": "CRO",
        "TEAM LEADER": "TEAM LEADER",
        "TECHNICIAN": "TECHNICIAN",
        "LOGISTIC": "LOGISTIC",
        "DRIVER": "DRIVER",
    }, max_length=100
    )

class Team(models.Model):
    team_lead = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='team_lead')
    team_members = models.ManyToManyField(Employees, related_name='team_members')
