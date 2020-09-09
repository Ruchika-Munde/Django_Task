from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from .models import Employee,Company
from .forms import EmpForm,CompForm

# Create your views here.

def display_view(request):
    c=Company.objects.all()
    return render(request,'display.html',{'c':c})

def add_view(request,id):
    obj=Company.objects.get(pk=id)
    empset=inlineformset_factory(Company,Employee,fields=('Ename',),)
    if request.method=='POST':
        form=empset(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/display/',id=obj.id)
    form=empset(instance=obj)
    return render(request,'add.html',{'form':form,'obj':obj})

def form(request):
    form=EmpForm()
    if request.method=='POST':
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/display/')
    return render(request,'form.html',{'form':form})

def comp_form(request):
    cform=CompForm()
    if request.method=='POST':
        cform=CompForm(request.POST)
        if cform.is_valid():
            cform.save()
            return redirect('/display/')
    return render(request,'cform.html',{'cform':cform})

