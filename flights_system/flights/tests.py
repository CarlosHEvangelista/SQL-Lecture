from multiprocessing.connection import Client
from django.test import TestCase

# Create your tests here.

from .models import AirportsAvailableModel, FlightSearchModel, PassengerListModel

class flightTestCase(TestCase):

    def setUp(self):
        a1 = AirportsAvailableModel.objects.create(code="AAA", city="City A")
        a2 = AirportsAvailableModel.objects.create(code="BBB", city="City B")

        FlightSearchModel.objects.create(Origin = a1, Destination = a2, Duration = 100)
        FlightSearchModel.objects.create(Origin = a1, Destination = a1, Duration = 100)
        FlightSearchModel.objects.create(Origin = a1, Destination = a2, Duration = -100)

    def test_departments_count(self):
        Departments = AirportsAvailableModel.objects.get(code = "AAA")
        self.assertEqual(Departments.departments.count(), 3)

    def test_alternatives_count(self):
        Alternatives = AirportsAvailableModel.objects.get(code = "AAA")
        self.assertEqual(Alternatives.alternatives.count(), 1)

    def test_valid_flight(self):
        a1 = AirportsAvailableModel.objects.get(code="AAA", city="City A")
        a2 = AirportsAvailableModel.objects.get(code="BBB", city="City B")
        Flight = FlightSearchModel.objects.get(Origin = a1, Destination = a2, Duration = 100)
        self.assertTrue(Flight.is_valid_flight())

    def test_invalid_destination(self):
        a1 = AirportsAvailableModel.objects.get(code="AAA")
        Flight = FlightSearchModel.objects.get(Origin = a1, Destination = a1, Duration = 100)
        self.assertFalse(Flight.is_valid_flight())

    def test_invalid_duration(self):
        a1 = AirportsAvailableModel.objects.get(code="AAA")
        a2 = AirportsAvailableModel.objects.get(code="BBB")
        Flight = FlightSearchModel.objects.get(Origin = a1, Destination = a2, Duration = -100)
        self.assertFalse(Flight.is_valid_flight())

    def test_index(self):
        Client = Client()
        Response = Client.get("/flights/")
        self.assertEqual(Response.status_code, 200)
        self.assertEqual(Response.context["flights"].count(), 3)