from django.shortcuts import render,redirect
from Userapp.models import User
from Userapp.forms import UserForm,LoginForm
from django.views import View
from django.contrib import messages
import hashlib
# Create your views here.

def make_password(password):
    assert password
    hash1=hashlib.md5(password.encode(encoding="utf-8")).hexdigest()
    return hash1

class UserRegistration(View):
    def get(self,request):
        userform=UserForm()
        return render(request,'UserRegistration.html',{'userform':userform})

    def post(self,request):
        userform=UserForm(request.POST)
        if userform.is_valid():
            password=userform.cleaned_data['password']
            cpassword=userform.cleaned_data['confirm_password']

            if(password==cpassword):
                password=make_password(password)
                cpassword=make_password(cpassword)
                user=User()
                user.name=userform.cleaned_data['name']
                user.username=userform.cleaned_data['username']
                user.password=password
                user.confirm_password=cpassword
                user.email=userform.cleaned_data['email']
                user.gender=userform.cleaned_data['gender']
                user.tag=userform.cleaned_data['tag']
                user.save()
                return redirect('/userapp/user_login/')
            else:
                return render(request,'UserRegistration.html',{'userform':userform} )

        else:
            return render(request,'UserRegistration.html',{'userform':userform} )

class UserLogin(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'UserLogin.html',{'form':form})

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            password=make_password(password)

            user=User.objects.get(username=username , password=password)
            if(user is not None):
                request.session['user']=user.username
                request.session['uid']=user.id
                return redirect('/postapp/showpost/')

            else:
                messages.error(request,'please enter valid username and password')
                return redirect('/userapp/user_login')
            
        else:
            messages.error(request,'Please enter valid username and password')
            return redirect('/userapp/user_login')