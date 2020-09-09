from django.shortcuts import render
from .models import Vehicle
# Create your views here.
def display_view(request):
    result=Vehicle.objects.all()
    return render(request,'index.html',{'result':result})