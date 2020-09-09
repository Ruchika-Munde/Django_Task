from django.shortcuts import render, HttpResponseRedirect
from Firstapp.models import Student
from Firstapp.forms import StudForm,NewStudentForm
# Create your views here.
def display_view(request):
    stud=Student.objects.all()
    return render(request,'display.html',{'stud':stud})

def add_view(request):
    adds=NewStudentForm()
    if request.method=='POST':
        form=NewStudentForm(request.POST)
        rollno=request.POST.get('rollno')
        name=request.POST.get('name')
        marks=request.POST.get('marks')
        addr=request.POST.get('addr')

        Student.objects.create(rollno=rollno,name=name,marks=marks,addr=addr)
        return HttpResponseRedirect('/display/')
    return render(request,'Add.html',{'adds':adds})

def update_view(request,id):
    data=Student.objects.get(pk=id)

    form=NewStudentForm()
    if request.method=='POST':
        #form=NewStudentForm(request.POST)
        rollno = request.POST.get('rollno')
        name = request.POST.get('name')
        marks = request.POST.get('marks')
        addr = request.POST.get('addr')
        Student.objects.create(rollno=rollno, name=name, marks=marks, addr=addr)
        return HttpResponseRedirect('/display')
    return render(request,'update.html',{'form':form,'data':data})

def delete_view(request,id):
    d=Student.objects.get(pk=id)
    d.delete()
    return render(request,'display.html')


