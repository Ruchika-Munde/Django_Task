from django.shortcuts import render,redirect
from .models import Summaryimages
from .forms import Summaryform
# Create your views here.

def show(request):
    obj=Summaryimages.objects.all()
    return render(request,'show.html',{'obj':obj})

def addimage(request):
    img=Summaryform()
    if (request.method=='POST'):
        img=Summaryform(request.POST,request.FILES)
        if img.is_valid() :
            img.save()

        return redirect('/show/')
    return render(request,'addform.html',{'img':img})