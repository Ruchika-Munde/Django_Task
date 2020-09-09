from django.db import models

# Create your models here.
class Clothes(models.Model):
    Catagory=models.TextField()
    Price=models.FloatField()
    Pattern=models.TextField()

    def __str__(self):
        return self.Catagory