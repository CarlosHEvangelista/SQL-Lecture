from django.contrib import admin

from .models import FlightSearchModel, AirportsAvailableModel

# Register your models here.

admin.site.register(AirportsAvailableModel)
admin.site.register(FlightSearchModel)
