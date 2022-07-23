from django.contrib import admin

from .models import FlightSearchModel, AirportsAvailableModel, PassengerListModel

# Register your models here.

class FlightSearchModelAdmin(admin.ModelAdmin):
    list_display = ("id", "Origin", "Destination", "Duration" )

class PessengerListModelAdmin(admin.ModelAdmin):
    filter_horizontal = ("flight",)

admin.site.register(AirportsAvailableModel)
admin.site.register(FlightSearchModel, FlightSearchModelAdmin)
admin.site.register(PassengerListModel, PessengerListModelAdmin)
