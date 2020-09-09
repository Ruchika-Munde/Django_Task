from django.shortcuts import render,redirect
from Commentapp.models import Comment
from django.views import View
from Commentapp.forms import commentform
from Postapp.models import Post
from Userapp.models import User
from Postapp.decorator import user_login
# Create your views here.

class Addcomment(View):
    @user_login
    def post(self,request,*args,**kwargs):
        cform=commentform(request.POST)
        id1 = kwargs.get('id')
        postobj = Post.objects.get(pk=id1)
        if cform.is_valid():
            comment = Comment()
            uid=request.session.get('uid')
            userobj = User.objects.get(pk=uid)
            comment.commentbox = cform.cleaned_data['commentbox']
            comment.commentforpost = postobj
            comment.commentbyuser = userobj
            if request.FILES:
                comment.cfileupload = cform.cleaned_data['cfileupload']
            comment.save()

        return redirect(f'/postapp/postdetail/{id1}/')

