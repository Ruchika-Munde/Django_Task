from django.db import models

# Create your models here.
class Employee(models.Model): #only for model form makemagrations and migrate
    eno=models.IntegerField() # this condition is used for validation=false
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.TextField()
    email=models.TextField()
    def __str__(self):
        return self.ename