from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .models import FlightSearchModel, PassengerListModel

def index(request):
    return render(request, 'flights/index.html', {
        'flights': FlightSearchModel.objects.all()
    })


def flightNumber(request, flight_id):
    flight = FlightSearchModel.objects.get(id=flight_id)
    return render (request, 'flights/flightNumber.html', {
        "flights": flight,
        'passengers': flight.passenger.all(),
        "non_passengers": PassengerListModel.objects.exclude(flight=flight).all()
    })

def book(request, flight_id):
    if request.method == 'POST':
        flight = FlightSearchModel.objects.get(id=flight_id)
        passenger = PassengerListModel.objects.get(id=int(request.POST["passenger"]))
        passenger.flight.add(flight)
        return HttpResponseRedirect(reverse("numberFlights", args=(flight.id,))) 