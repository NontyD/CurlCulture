from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_service, name='bookings_home'),  # This matches /bookings/
    path('book/', views.book_service, name='booking_form'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('services/', views.services_view, name='services'),
    path('services/<str:category>/', views.services_view, name='services'),  # New URL for category services
    path('book/<int:service_id>/', views.book_service, name='book_service'),  # URL for booking a specific service
    path('search/', views.search, name='search'),
]
