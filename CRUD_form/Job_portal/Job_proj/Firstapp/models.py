from django.db import models

# Create your models here.
class privatejob(models.Model):
    padd1=models.TextField()
    padd2=models.TextField()
    padd3=models.TextField()
    padd4=models.TextField()
    padd5=models.TextField()
    padd6=models.TextField()

    def __str__(self):
        return self.padd1