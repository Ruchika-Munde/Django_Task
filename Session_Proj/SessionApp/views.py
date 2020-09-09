from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
    user = request.session.get('user')
    #del request.session['user']
    #request.session.set_expiry(60)
    if user:
        print('hii user')
        return render(request, 'home.html', {'user': user})
    else:
        print('hii else')
        return render(request, 'login.html')


def login(request):
    if request.session.has_key('user'):
        return redirect('/home/')

    if (request.method == 'POST'):
        username = request.POST['txtuname']
        password = request.POST['txtpass']
        try:
            user = auth.authenticate(username=username, password=password)
            if (user is not None):
                auth.login(request, user)
                request.session['user'] = user.username
                request.session.set_expiry(30)
                return redirect('/home/')
        except (auth.ObjectDoesNotExist):
            print('Error')
    return render(request, 'login.html')
