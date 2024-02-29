from django.db import models

# Create your models here.
class Companies(models.Model):
    name_of_company = models.CharField(max_length=60)
    Phone_number = models.CharField(max_length=30)
    Phone_number_2 = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)



class Clients(models.Model):
    companies=models.ForeignKey(Companies,on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=60)
    Tin_number = models.CharField(max_length=60)
    Main_contact_person_full_name = models.CharField(max_length=30)
    Main_contact_person_phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    physical_address = models.CharField(max_length=100)
    Structural_detail = models.CharField(max_length=60)

