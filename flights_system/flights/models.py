from django.db import models

# Create your models here.

class AirportsAvailableModel(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} ({self.city})"

class FlightSearchModel(models.Model):
    Origin = models.ForeignKey(AirportsAvailableModel, on_delete=models.CASCADE, related_name="departments")
    Destination = models.ForeignKey(AirportsAvailableModel, on_delete=models.CASCADE, related_name="alternatives")
    Duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.Origin} to {self.Destination}"


class PassengerListModel(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    flight = models.ManyToManyField(FlightSearchModel, blank=True, related_name="passenger")

    def __str__(self):
        return f"{self.firstName} {self.lastName}"