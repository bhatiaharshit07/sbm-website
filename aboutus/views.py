from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
import os
from django.views.generic import ListView
from .models import CarouselHome
from .models import NewsHome

# Create your views here.

class HomePageView(ListView):
    context_object_name = 'carousel_list'
    template_name = 'home.html'
    queryset = CarouselHome.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['news_list'] = NewsHome.objects.all()
        context['my_url_home'] = "http://www.samskritisansthan.com"
        return context


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

