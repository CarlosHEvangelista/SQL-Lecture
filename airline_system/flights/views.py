from django.shortcuts import render

# Create your views here.

from .models import Flight

def Flights(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })