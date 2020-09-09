from django.db import models

# Create your models here.
class Vehicle(models.Model):
    Brand=models.TextField(max_length=30)
    Model=models.TextField()
    Price=models.FloatField()
    Average=models.IntegerField()