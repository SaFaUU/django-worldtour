from django.db import models

# Create your models here.
class Trip(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    nights = models.IntegerField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id} - {self.origin} TO {self.destination} for {self.nights}, costs {self.price} EUR"