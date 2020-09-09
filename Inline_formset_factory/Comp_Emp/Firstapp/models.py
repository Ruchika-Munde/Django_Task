from django.db import models

# Create your models here.
class Company(models.Model):
    Cname=models.CharField(max_length=30)

    def __str__(self):
        return self.Cname

class Employee(models.Model):
    Ename=models.CharField(max_length=30)
    comp=models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.Ename


