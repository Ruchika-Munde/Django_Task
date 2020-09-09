from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField(blank=True,null='') # this condition is used for validation=false
    sname=models.CharField(max_length=30,blank=True,null='')
    marks=models.FloatField(blank=True,null='')
    addr=models.CharField(max_length=30,blank=True,null='')

    def __str__(self):
        return self.sname