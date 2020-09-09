from django.shortcuts import render
from UserRegistration.forms import UserRegistrationForm
# Create your views here.


#** Add field in exsting form using UserRegistrationForm **
def user(request):
    if request.method=='POST':
        obj=UserRegistrationForm(request.POST)
        if obj.is_valid():
            obj.save()
    obj=UserRegistrationForm()
    return render(request,'view.html',{'obj':obj})

# ***login logout ***
def success(request):
    return render(request,'success.html')