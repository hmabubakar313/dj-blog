from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()




def home(request):
    return render(request, 'base.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        print('first_name', first_name)
        print('last_name', last_name)
        
        user = User.objects.create_user(email=email, password=password, username=username, first_name=first_name, last_name=last_name)
        print('saving user', user)
        user.save()
        return redirect('login')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        if user is not None:
            if user.check_password(password):
                return redirect('home')
            else:
                return HttpResponse('Password is incorrect')
        else:
            return HttpResponse('User does not exist')
    else:
        return render(request, 'login.html')

