from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name