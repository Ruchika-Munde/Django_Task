from django.db import models

# Create your models here.
class Vehicle(models.Model):
    Brand=models.CharField(max_length=30)
    Model=models.CharField(max_length=30)
    Price=models.IntegerField()
    Average=models.CharField(max_length=30)

    def __str__(self):
        return self.Brand