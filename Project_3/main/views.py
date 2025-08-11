from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Service
from .models import SubService
import datetime

def services_list(request):
    services= Service.objects.all()
    subservice= SubService.objects.all()
    return render(request, 'main/services_list.html',{'services':services})

def index(request):
    services= Service.objects.all()
    return render(request, 'main/index.html',{'services':services})

def calendar(request):
    services= Service.objects.all()
    # Lista dni (np. Poniedziałek–Niedziela)
    start_date = datetime.date.today()
    week_days = [(start_date + datetime.timedelta(days=i)) for i in range(7)]

    # Lista godzin np. od 8:00 do 18:00 co 1h
    hours = [f"{h:02d}:00" for h in range(8, 19)]
    return render(request, 'main/calendar.html',{'services':services, 'week_days': week_days,
        'hours': hours})

def reservation(request):
    services= Service.objects.all()
    return render(request, 'main/reservation.html',{'services':services})

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

def chat_bot_view(request):
    user_message = request.GET.get("message", "").lower()

    # Proste warunki

    if "hello" in user_message:
        reply = "Hi there! How can I help you?"
    elif "bye" in user_message:
        reply = "Goodbye! Have a great day!"
    else:
        reply = f"You said: {user_message}"

    return JsonResponse({"reply": reply})

def chat_bot_page(request):
    return render(request, 'main/chatbot.html')