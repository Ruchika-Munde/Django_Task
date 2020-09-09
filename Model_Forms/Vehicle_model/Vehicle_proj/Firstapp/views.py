from django.shortcuts import render,HttpResponseRedirect
from .models import Vehicle
from .forms_add import VehicleReg
# Create your views here.

#**To show / display data on browser
def display_view(request):
    result=Vehicle.objects.all()
    return render(request,'display.html',{'result':result})

#** To add/ insert data using model forms

def add_view(request):
    if request.method=='POST':
        add=VehicleReg(request.POST)
        if add.is_valid():
            add.save()
            return HttpResponseRedirect('/display/')
    else:
        add=VehicleReg()
        return render(request,'forms_add.html',{'add':add})

# ** to update data using model forms

def update_view(request,id):
    data=Vehicle.objects.get(pk=id)
    form=VehicleReg(instance=data)
    if request.method=='POST':
        form=VehicleReg(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/display/')
    return render(request,'forms_update.html',{'form':form,'data':data})

def delete_view(request,id):
    d=Vehicle.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('/display/')