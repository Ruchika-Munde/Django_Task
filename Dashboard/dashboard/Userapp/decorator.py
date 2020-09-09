from django.shortcuts import redirect

def user_login(function):
    print(function.__name__)
    def wrap(self,request,*args,**kwargs):
        if request.session.get('uid'):
            print(request.session.get('uid',None))
            return function(self,request,*args,**kwargs)
        else:
            return redirect('/userapp/user_login/')
    return wrap
