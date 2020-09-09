from django.db import models

# Create your models here.
class Summaryimages(models.Model):
    imagename=models.CharField(max_length=30)
    Image = models.ImageField(upload_to='images/')
    summary=models.TextField()


    def __str__(self):
        return self.imagename
