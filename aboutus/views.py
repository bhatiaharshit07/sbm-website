from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
import os
from django.views.generic import ListView
from .models import CarouselHome
from .models import NewsHome1

# Create your views here.

class HomePageView(ListView):
    model = CarouselHome
    template_name = 'home.html'



def home(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, 'aboutus.html')
    

def infrastructure(request):
    return render(request, "infrastructure.html")

def admission(request):
    return render(request, "admission.html")

def facilities(request):
    return render(request, "facilities.html")

def gallery(request):
    return render(request, "gallery.html")

def contacts(request):
    return render(request, "contacts.html")

