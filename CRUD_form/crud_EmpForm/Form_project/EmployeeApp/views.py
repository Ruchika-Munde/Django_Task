from django.shortcuts import render,HttpResponseRedirect
from .models import Employee
# Create your views here.
def display_view(request):
    result=Employee.objects.all()
    return render(request,'EmpDetails.html',{'result':result})

def Add_view(request):
    print(request.POST)
    a1=request.POST['txtname']
    a2=request.POST['txtcomp']
    a3=request.POST['txtdesi']
    a4=request.POST['txtsal']

    b=Employee(Name=a1,Company=a2,Designation=a3,Salary=a4)
    b.save()
    return HttpResponseRedirect ('/display/')

def Delete_view(request,id):
    d=Employee.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('/display/')

def Update_view(request,id):
    obj=Employee.objects.get(pk=id)
    if request.method=='POST':
        obj.Name=request.POST['txtuname']
        obj.Company = request.POST['txtucomp']
        obj.Designation = request.POST['txtudesi']
        obj.Salary= request.POST['txtusal']
        obj.save()
        return HttpResponseRedirect('/display/')
    return render(request,'update.html',{'obj':obj})