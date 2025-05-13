from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_service, name='bookings_home'),  # This matches /bookings/
    path('book/', views.book_service, name='booking_form'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('services/', views.services_view, name='services'),
]
