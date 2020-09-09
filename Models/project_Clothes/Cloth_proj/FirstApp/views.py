from django.shortcuts import render
from .models import Clothes
# Create your views here.

def index1(request):
    result=Clothes.objects.all()
    return render(request,'index.html',{'result':result})