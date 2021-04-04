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

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})