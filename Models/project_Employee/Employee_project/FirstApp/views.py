from django.shortcuts import render
from FirstApp.models import Employee


# Create your views here.


def display_view(request):
    result=Employee.objects.all()
    return render(request,'index.html',{'result':result})


