from django.shortcuts import render,HttpResponseRedirect
from Firstapp.models import Employee
from Firstapp.forms import NewEmployeeForm
from django.forms import modelformset_factory # Inline form
# Create your views here.
def display_view(request):
    e=Employee.objects.all()
    return render(request,'display.html',{'e':e})

def delete_view(request,id):
    d=Employee.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('/display/')

def add_view(request):
    # ef = EmployeeForm()  #for model form
    ef=NewEmployeeForm()    # for Django form
    if request.method=='POST':
        #Form=EmployeeForm(request.POST) #for modelform
        Form = NewEmployeeForm(request.POST) #for Django form
        print(request.POST)
        eno=request.POST.get('eno')
        ename=request.POST.get('ename')
        esal=request.POST.get('esal')
        eaddr=request.POST.get('eaddr')
        email=request.POST.get('email')
        # ** 1) to create/ save all data in django form
        obj=Employee(eno=eno,ename=ename,esal=esal,eaddr=eaddr,email=email)
        obj.save()
        return HttpResponseRedirect('/display/')
        # ** 2) to create/ save all data in django form
        # Employee.objects.create(
        #     eno=eno,ename=ename,esal=esal,eaddr=eaddr,email=email
        # )
        #print(eno,ename,esal,eaddr,email)

         #**model forms
        #if Form.is_valid():
            #Form.save()
    return render(request,'form.html',{'ef':ef})

def update_view(request,id):
    data=Employee.objects.get(pk=id) #e contains object
    initial={'eno':data.eno,'ename':data.ename,'esal':data.esal,'eaddr':data.eaddr,'email':data.email}
    Form=NewEmployeeForm(initial=initial) #send data to form
    if request.method=='POST':
        Form=NewEmployeeForm(request.POST)#update logic
        if Form.is_valid():
            data.eno = request.POST.get('eno')
            data.ename = request.POST.get('ename')
            data.esal = request.POST.get('esal')
            data.eaddr = request.POST.get('eaddr')
            data.email = request.POST.get('email')
            data.save()
        # ** 1) to create/ save all data in django form
        # obj = Employee(eno=eno, ename=ename, esal=esal, eaddr=eaddr, email=email)
        # obj.save()
        return HttpResponseRedirect('/display/')
    return render(request,'formupdate.html',{'Form':Form,'data':data}) #how to object pass for update data


#** model form
# def update_view(request,id):
#     data=Employee.objects.get(pk=id) # data contains object
#     Form=EmployeeForm(instance=data) # send data to form
#     if request.method=='POST':
#         Form=EmployeeForm(request.POST,instance=data) # update logic
#         if Form.is_valid():
#             Form.save()
#         return HttpResponseRedirect('/display/')
#     return render(request,'formupdate.html',{'Form':Form,'data':data})




