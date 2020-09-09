from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.TextField()
    Company=models.TextField()
    Designation=models.TextField()
    Salary=models.FloatField()
