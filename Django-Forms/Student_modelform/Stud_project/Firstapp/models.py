from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    rollno=models.IntegerField()
    name=models.TextField()
    marks=models.FloatField()
    addr=models.TextField()

    def __str__(self):
        return self.name