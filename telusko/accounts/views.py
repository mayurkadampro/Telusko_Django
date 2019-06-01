from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == 'POST':
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirmPassword = request.POST['password2']

        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=firstName,last_name=lastName)
                user.save();
                messages.info(request,'new user created')
                
        else:
            messages.info(request,'password is not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')