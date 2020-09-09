from django.shortcuts import render,HttpResponseRedirect
from django.views import View

# Create your views here.

#funtion base view
def display(request):
    return render(request,'display.html')

#class base view

class Student(View):
    def get(self,request,**kwargs):  # name of method must be given as only get
        print(kwargs)           # to get id
        return render(request,'get.html')

    def post(self,request,**kwargs): # name of method must be given as only post
        return render(request,'post.html')


