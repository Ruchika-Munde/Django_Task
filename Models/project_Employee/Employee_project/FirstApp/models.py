from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=30)
    Company=models.TextField()
    Salary=models.IntegerField()
    Experience=models.FloatField()

