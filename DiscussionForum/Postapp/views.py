from django.shortcuts import render,redirect
from Postapp.forms import Addpostform
from Postapp.models import Post
from django.views import View
from Userapp.models import User
from Commentapp.forms import commentform
from Postapp.decorator import user_login
# Create your views here.

#for add post
class base(View):
    def get(self,request):
        return render(request,'base.html')

class Addpost(View):
    @user_login
    def get(self,request):
        pform=Addpostform()
        return render (request,'post.html',{'pform':pform})
    
    def post(self,request,*args,**kwargs):
        pform=Addpostform(request.POST,request.FILES)
        if(pform.is_valid()):
            post=Post(title=pform.cleaned_data['title'],description=pform.cleaned_data['description'],ptag=pform.cleaned_data['ptag'])
            if(request.FILES):
                post.fileupload = pform.cleaned_data['fileupload']
            uid=request.session.get('uid')
            print(uid)
            user_obj=User.objects.get(pk=uid)
            post.postbyuser=user_obj
            post.save()
            return redirect('/postapp/showpost/')

 
# for show post
class posttitle(View):
    def get(self,request):
        obj=Post.objects.all()
        return render(request,'home.html',{'obj':obj})

# show post details
class postdetails(View):
    def get(self,request,id):
        pobj=Post.objects.get(pk=id)
        form = commentform()
        return render(request,'postdetails.html',{'pobj':pobj,'form':form})
