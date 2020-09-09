from django.shortcuts import render,HttpResponseRedirect
from .models import Mobile
from .forms_add import MobileReg
# Create your views here.

#**To show / display data on browser
def display_view(request):
    result=Mobile.objects.all()
    return render(request,'display.html',{'result':result})

#** To add/ insert data using model forms

def add_view(request):
    if request.method=='POST':
        add=MobileReg(request.POST)
        if add.is_valid():
            add.save()
            return HttpResponseRedirect('/display/')
    else:
        add=MobileReg()
        return render(request,'forms_add.html',{'add':add})

# ** to update data using model forms

def update_view(request,id):
    data=Mobile.objects.get(pk=id)
    form=MobileReg(instance=data)
    if request.method=='POST':
        form=MobileReg(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/display/')
    return render(request,'forms_update.html',{'form':form,'data':data})

def delete_view(request,id):
    d=Mobile.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('/display/')