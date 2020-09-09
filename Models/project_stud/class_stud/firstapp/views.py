from django.shortcuts import render
from firstapp.models import Student
# Create your views here.
# class Student:
#     rollno=0
#     name=''

def index(request):

    return render(request,'index.html',{'data':{'Name':'Rucha', 'RollNO':101}})

def display_view(request):
    result=Student.objects.all()
    return render(request,'index.html',{'result':result})