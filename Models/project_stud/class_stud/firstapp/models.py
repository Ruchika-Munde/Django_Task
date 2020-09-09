from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=30)
    Rollno=models.IntegerField()
    Marks=models.FloatField()
    Address=models.TextField()

    def __str__(self):
        return self.Name