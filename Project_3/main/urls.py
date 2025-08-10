from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('services_list/', views.services_list, name='services_list'),
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('calendar/', views.calendar ,name='calendar'),
    path('reservation/', views.reservation ,name='reservation'),
    ]