from django.shortcuts import render
from .models import Task

def services_list(request):
    services= Task.objects.all()
    return render(request, 'main/services_list.html',{'services':services})

def index(request):
    services= Task.objects.all()
    return render(request, 'main/index.html',{'services':services})

def resume(request):
    services= Task.objects.all()
    return render(request, 'main/about_me.html',{'services':services})


    

