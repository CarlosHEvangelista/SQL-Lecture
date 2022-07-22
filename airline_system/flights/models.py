from django.db import models

# Create your models here.
class Airplane(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)



class Flight(models.Model):
    origin = models.ForeignKey("Airplane", on_delete=models.CASCADE, related_name="Department")
    destination = models.ForeignKey("Airplane", on_delete=models.CASCADE, related_name="Alternative")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"