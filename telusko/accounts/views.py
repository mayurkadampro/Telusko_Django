from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

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
                print('username is already taken')
            elif User.objects.filter(email=email).exists():
                print('email is already taken')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=firstName,last_name=lastName)
                user.save();
                print('new user created')
        else:
            print('password is not matching')
        return redirect('/')
    else:
        return render(request,'register.html')