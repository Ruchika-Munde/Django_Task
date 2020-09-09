from django.shortcuts import render,HttpResponseRedirect
from . models import privatejob
# Create your views here.
def display(request):
    return render(request,'display.html')

def addprivate(request):
    if request.method=='POST':
        a1=request.POST['txtpadd1']
        a2=request.POST['txtpadd2']
        a3=request.POST['txtpadd3']
        a4=request.POST['txtpadd4']
        a5=request.POST['txtpadd5']
        a6=request.POST['txtpadd6']

        b=privatejob(padd1=a1,padd2=a2,padd3=a3,padd4=a4,padd5=a5,padd6=a6)
        b.save()
        return HttpResponseRedirect('/display/')
    return render(request,'private.html')
