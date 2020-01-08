from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
#login authentication###################
        if user is not None:
            auth.login(request,user)
            print('user logged in ')
            return redirect('/')
        else:
            messages.info(request, 'Invalid user name or password')
            return redirect('login')
    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        #password validations
        if (password_1 == password_2):

            user= User.objects.create_user(username=username,password=password_1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print('user created')
            return redirect('/')
        else:
            return redirect('/account/register')
    else:
        return render(request, 'register.html')