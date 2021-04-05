from django.contrib import admin
from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('infrastructure', views.infrastructure, name="infrastructure"),
    path('admission', views.admission, name="admission"),
    path('facilities', views.facilities, name="facilities"),
    path('gallery', views.gallery, name="gallery"),
    path('contacts', views.contacts, name="contacts"),    
]