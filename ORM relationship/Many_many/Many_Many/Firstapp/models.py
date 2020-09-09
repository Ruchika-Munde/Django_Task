from django.db import models

# Create your models here.
class Address(models.Model):
    aid=models.AutoField(primary_key=True)
    area_name=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    #change the name of table or class in database i.e. firstapp_Address change to address using Meta class
    class Meta:
        db_table='Address'
    def __str__(self):
        return f'{self.area_name,self.city}'

class Employee(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=30)
    ecom=models.CharField(max_length=30)
    esal=models.IntegerField()
    eaddr=models.ForeignKey(Address,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.ename}'

class Language(models.Model):
    lid=models.AutoField(primary_key=True)
    lname=models.CharField(max_length=20)
    employee=models.ManyToManyField(Employee)
    def __str__(self):
        return f'{self.lname}'