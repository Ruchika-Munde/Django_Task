from django.db import models

# Create your models here.
class Mobile(models.Model):
    Brand=models.CharField(max_length=30)
    ModelName=models.TextField()
    Price=models.FloatField()
    Ram=models.TextField()

    def __str__(self):
        return self.Brand