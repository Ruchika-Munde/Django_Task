from django.shortcuts import render,HttpResponseRedirect
from .models import Employee
from .forms import Empreg
from django.contrib.auth.decorators import login_required
# Create your views here.

# view for to insert/ add data with forms.html
@login_required(login_url='/login/')
def view(request):
    if request.method=='POST':
        e=Empreg(request.POST)

        if e.is_valid():
            e.save()
            return HttpResponseRedirect('/fa/form_display/')
    else:
        e=Empreg()
        return render(request,'forms.html',{'e':e})

# display for to show data with display.html
@login_required(login_url='/login/')
def display(request):
    result=Employee.objects.all()
    return render(request,'display.html',{'result':result})


@login_required(login_url='/login/')
def delete(request,id):
    d=Employee.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('/fa/form_display/')

@login_required(login_url='/login/')
def update(request,id):
    data=Employee.objects.get(pk=id)
    form=Empreg(instance=data)
    if request.method=='POST':
        form=Empreg(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/fa/form_display/')
    return render(request,'update.html',{'form':form,'data':data})

