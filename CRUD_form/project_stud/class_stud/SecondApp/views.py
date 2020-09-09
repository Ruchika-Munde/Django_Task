from django.shortcuts import render,HttpResponseRedirect
from .models import Form
# Create your views here.
def display(request):
    print(request.POST)
    result=Form.objects.all()
    return render(request,'secondapp.html',{'result':result})

def add(request):
    #request.post.get()
    a=request.POST['txtName']   #txtName is name of text in secondapp.html
    b=Form(Name=a)     #Name is field name i.e. in models.py
    b.save()
    return HttpResponseRedirect('/sa/display/')

def delete(request,id):
    c=Form.objects.get(pk=id)
    c.delete()
    return HttpResponseRedirect('/sa/display/')

def update(request,id):
    obj=Form.objects.get(pk=id)
    if request.method=='POST':
        obj.Name=request.POST['txtupdate']
        obj.save()
        return HttpResponseRedirect ('/sa/display/')
    return render(request,'update.html',{'obj':obj})
