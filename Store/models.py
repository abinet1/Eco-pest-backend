from django.db import models

# Create your models here.
class Medicines(models.Model):
    name_of_medicine = models.CharField(max_length=30)
    Role = {
        "CEO": "CEO",
        "CRO": "CRO",
        "TEAM LEADER": "TEAM LEADER",
        "TECHNICIAN": "TECHNICIAN",
        "LOGISTIC": "LOGISTIC",
        "DRIVER": "DRIVER",
     
    }
    quantity = models.IntegerField()
    unit_measurement={
        "lt": "litter",
        "g": "gram",
    }
