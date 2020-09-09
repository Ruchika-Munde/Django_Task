from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentReg
from .models import Student
# Create your views here.

#this form contains data

def view(request):
    if request.method=='POST':
        s=StudentReg(request.POST)

        if s.is_valid():
            s.save()
        return HttpResponseRedirect('/form/form_view/')

    else:
        s=StudentReg()
        return render(request,'forms.html',{'s':s})

def display1(request):
    result=Student.objects.all()
    return render(request,'display.html',{'result':result})

def delete(request,id):
    d=Student.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('/form/form_display/')


#** HTML forms
# def update(request,id):
#     obj=Student.objects.get(pk=id) # manually for update.html
#     u=StudentReg()
#     if request.method=='POST':
#         obj.sid=request.POST['txtsid']
#         obj.sname=request.POST['txtsname']
#         obj.marks=request.POST['txtmarks']
#         obj.addr=request.POST['txtaddr']
#         obj.save()
#         return HttpResponseRedirect('/form/form_display/')
#     return render(request,'update.html',{'obj':obj,'u':u})


def update1(request,id):
    data=Student.objects.get(pk=id)
    form=StudentReg(instance=data)
    if request.method=='POST':
        form=StudentReg(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/form/form_display/')
    return render(request,'update1.html',{'form':form,'data':data})