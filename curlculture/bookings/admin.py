# bookings/admin.py
from django.contrib import admin
from .models import ServiceCategory, SalonService, Booking, ContactMessage

admin.site.register(ServiceCategory)
admin.site.register(SalonService)
admin.site.register(Booking)
admin.site.register(ContactMessage)