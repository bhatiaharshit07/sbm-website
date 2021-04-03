from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('aboutus/principal-desk', views.principal_desk, name="principal_desk"),
    path('aboutus/management-desk', views.management_desk, name="management_desk"),
    path('aboutus/management', views.management, name="management"),
]