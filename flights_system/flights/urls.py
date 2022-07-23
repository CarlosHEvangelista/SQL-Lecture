from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="indexFlights"),
    path("<int:flight_id>", views.flightNumber, name="numberFlights"),
    path("<int:flight_id>/book", views.book, name="book")
]