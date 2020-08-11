from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == 'POST':

        # get data from POST
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # create user object from data
        if password != confirm_password:
            messages.info(request,'Password mismatch.')
            return render(request, 'register.html')
        if User.objects.filter(username=username).exists():
            messages.info(request,'username taken.')
            return render(request, 'register.html')
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        messages.info(request,'user created')
        auth.login(request, user)
        return redirect('/')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is None:
        messages.info(request, 'Login Failed')
        return render(request, 'login.html')
    auth.login(request, user)
    return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')
