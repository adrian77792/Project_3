from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Service, Reservation
from .models import SubService
from collections import OrderedDict
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
    reservations = Reservation.objects.select_related("service").filter(date__in=week_days)
    reserved_slots = [
    {
        "date": r.date,
        "time": r.time.strftime("%H:%M"),
        "service": r.service.title,
        "service_duration": r.service.time,
    }
    for r in reservations
]
    # Lista godzin np. od 8:00 do 18:00 co 1h
    hours = [f"{h:02d}:00" for h in range(8, 19)]
    return render(request, 'main/calendar.html',{'services':services, 'week_days': week_days,
        'hours': hours, 'reserved_slots': reserved_slots})

def calendar_view(request):
    services = Service.objects.all()
    start_date = datetime.date.today()
    week_days = [(start_date + datetime.timedelta(days=i)) for i in range(7)]
    hours = [f"{h:02d}:00" for h in range(8, 19)]

    # pobieramy wszystkie rezerwacje w tym tygodniu
    reservations = Reservation.objects.select_related("service").filter(
        date__range=(start_date, start_date + datetime.timedelta(days=6))
    )

    # budujemy listę dni z godzinami i slotami
    calendar_list = []
    for day in week_days:
        day_str = day.strftime("%Y-%m-%d")
        hours_list = []
        for hour in hours:
            matching_slots = [
                {
                    "service": r.service.title,
                    "duration": r.service.time,
                    "time": r.time.strftime("%H:%M")
                }
                for r in reservations
                if r.date.strftime("%Y-%m-%d") == day_str and r.time.strftime("%H:%M") == hour
            ]
            hours_list.append({"hour": hour, "slots": matching_slots})
        calendar_list.append({"day": day_str, "hours": hours_list})

    return render(request, "main/calendar.html", {
        "services": services,
        "calendar_list": calendar_list,
        "week_days": week_days,
        "hours": hours,
    })

def reservation(request):
    services= Service.objects.all()
    hours = [f"{h:02d}:00" for h in range(8, 19)]
    if request.method == "POST":
        service_id = request.POST.get("service")
        date = request.POST.get("date")
        time = request.POST.get("hour")
        time_obj = datetime.datetime.strptime(time, "%H:%M").time()

        service = Service.objects.get(id=service_id)
        Reservation.objects.create(
            service=service,
            date=date,
            time=time_obj
        )
        return redirect("calendar")
    return render(request, 'main/reservation.html',{'services':services, 'hours':hours})

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