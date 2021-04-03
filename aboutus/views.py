from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def home(request):
    return render(request, "base.html")

def aboutus(request):
    return render(request, "base.html")

def principal_desk(request):
    return HttpResponse("Principal Desk")

def management_desk(request):
    return HttpResponse("management Desk")

def management(request):
    return HttpResponse("management")