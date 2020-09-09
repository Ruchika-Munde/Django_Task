from django.shortcuts import render
from .models import Mobile
# Create your views here.
def display1(request):
    result=Mobile.objects.all()
    return render(request,'index.html',{'result':result})