from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from Firstapp.forms import UserRegistrationForm
# Create your views here.

#** User creation form ***
'''def user(request):
    if request.method=='POST':
        obj=UserCreationForm(request.POST)
        obj.save()
    obj=UserCreationForm()
    return render(request,'view.html',{'obj':obj})'''

#** Add field in exsting form using UserRegistrationForm **
def user(request):
    if request.method=='POST':
        obj=UserRegistrationForm(request.POST)
        if obj.is_valid():
            obj.save()
        return redirect('/login/')
    obj=UserRegistrationForm()
    return render(request,'view.html',{'obj':obj})

# ***login logout ***
def display(request):
    return render(request,'display.html')