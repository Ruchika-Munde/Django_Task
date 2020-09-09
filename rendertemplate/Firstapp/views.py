from django.shortcuts import render,redirect
from Firstapp.forms import StudentForm
from Firstapp.models import Student
# Create your views here.

def Add(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/firstapp/show/')
    return render(request,'home.html',{'form':form})

def Show(request):
    data=Student.objects.all()
    return render(request,'show.html',{'data':data})
        