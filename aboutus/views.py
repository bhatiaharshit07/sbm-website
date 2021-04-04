from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import ImageForm
# Create your views here.
def home(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "aboutus.html")

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

