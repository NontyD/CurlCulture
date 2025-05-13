from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey('SalonService', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name} on {self.date} at {self.time}"
    

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SalonService(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.DurationField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    hair_provided = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (€{self.price})"
