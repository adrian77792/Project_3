from django.urls import path
from . import views

urlpatterns = [
    path('services_list/', views.services_list, name='services_list'),
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    ]