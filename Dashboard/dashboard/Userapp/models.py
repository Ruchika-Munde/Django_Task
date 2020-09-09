from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserReg(models.Model):
    Name=models.CharField(max_length=30)
    Username=models.CharField(max_length=30,unique=True)
    Password=models.CharField(max_length=30)
    Confirmpassword=models.CharField(max_length=30)
    Email=models.EmailField()
    Mobileno=PhoneNumberField(blank=True)
    Address=models.CharField(max_length=30)
    Resume=models.FileField(upload_to='FileUpload/')
    

    def __str__(self):
        return self.Username



