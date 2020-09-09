from django.db import models

# Create your models here.
class State(models.Model):
    Sname=models.CharField(max_length=30)

    def __str__(self):
        return self.Sname

class District(models.Model):
    Dname=models.CharField(max_length=30)
    MH=models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.Dname