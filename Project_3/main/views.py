from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Service
from .models import SubService

def services_list(request):
    services= Service.objects.all()
    subservice= SubService.objects.all()
    return render(request, 'main/services_list.html',{'services':services})

def index(request):
    services= Service.objects.all()
    return render(request, 'main/index.html',{'services':services})

def resume(request):
    services= Service.objects.all()
    return render(request, 'main/about_me.html',{'services':services})

def services(request):
    services= Service.objects.all()
    subservice= SubService.objects.all()
    return render(request, 'main/services.html',{'services':services})

def user_login(request):
    #login= Service.objects.all()
    #subservice= SubService.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
 
        if user is not None:
            login(request, user)
            return redirect('index.html')  # Redirect to homepage or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
 
    return render(request, 'login.html')