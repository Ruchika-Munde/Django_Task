from django.db import models

# Create your models here.
class Mobile(models.Model):
    Mname=models.CharField(max_length=30)
    Brand=models.CharField(max_length=30)
    Price=models.IntegerField()
    Ram=models.CharField(max_length=30)

    def __str__(self):
        return self.Brand