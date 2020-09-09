from django.shortcuts import redirect

def user_login(function):
    print(function.__name__)
    def wrap(self,request,*args,**kwargs):
        if request.session.get('user'):
            print(request.session.get('user',None))
            return function(self,request,*args,**kwargs)
        else:
            return redirect('/userapp/user_login/')
    return wrap
