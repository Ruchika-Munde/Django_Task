from django.shortcuts import render,HttpResponseRedirect
from .models import Employee
from .forms import Empreg
# Create your views here.

# view for to insert/ add data with forms.html
def view(request):
    if request.method=='POST':
        e=Empreg(request.POST)

        if e.is_valid():
            e.save()
            return HttpResponseRedirect('/form/form_display/')
    else:
        e=Empreg()
        return render(request,'forms.html',{'e':e})

# display for to show data with display.html
def display(request):
    result=Employee.objects.all()
    return render(request,'display.html',{'result':result})

def delete(request,id):
    d=Employee.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('/form/form_display/')

def update(request,id):
    data=Employee.objects.get(pk=id)
    form=Empreg(instance=data)
    if request.method=='POST':
        form=Empreg(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/form/form_display/')
    return render(request,'update.html',{'form':form,'data':data})

# def update(request,id):
#     obj=Employee.objects.get(pk=id)
#     u=Empreg()
#
#     if request.method=='POST':
#         obj.eid=request.POST['txteid']
#         obj.ename=request.POST['txtename']
#         obj.designation=request.POST['txtdesign']
#         obj.salary=request.POST['txtsal']
#         obj.save()
#         return HttpResponseRedirect('/form/form_display/')
#     return render(request,'update.html',{'obj':obj,'u':u})