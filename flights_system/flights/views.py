from django.shortcuts import render

# Create your views here.

from .models import FlightSearchModel

def index(request):
    return render(request, 'flights/index.html', {
        'flights': FlightSearchModel.objects.all()
    })


def flightNumber(request, flight_id):
    flight = FlightSearchModel.objects.get(id=flight_id)
    return render (request, 'flights/flightNumber.html', {
        "flights": flight
    })