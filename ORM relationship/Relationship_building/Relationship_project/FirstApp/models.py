from django.db import models

# Create your models here.
class Language(models.Model): #one to many
    Lname=models.CharField(max_length=30)

    def __str__(self):
        return self.Lname

class Framework(models.Model): #one to many
    Fname=models.CharField(max_length=30)
    Lang=models.ForeignKey(Language,on_delete=models.CASCADE)

    def __str__(self):
        return self.Fname


class Movies(models.Model): #many to many
    Mname=models.CharField(max_length=30)
    def __str__(self):
        return self.Mname

class Character(models.Model): #many to many
    Cname=models.CharField(max_length=30)
    movies=models.ManyToManyField(Movies)

    def __str__(self):
        return self.Cname




