from django.shortcuts import render
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


