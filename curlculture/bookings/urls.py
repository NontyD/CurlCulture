from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_service, name='bookings_home'),  # This matches /bookings/
    path('book/', views.book_service, name='book_service'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
]
