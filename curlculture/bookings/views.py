from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from .models import ServiceCategory, SalonService


@login_required
def book_service(request):
    service_id = request.GET.get('service_id')
    form = BookingForm(initial={'service': service_id}) if service_id else BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_confirmation')

    return render(request, 'bookings/book_service.html', {'form': form})


def booking_confirmation(request):
    return render(request, 'bookings/booking_confirmation.html')


def services_view(request):
    categories = ServiceCategory.objects.prefetch_related('salonservice_set').all()
    return render(request, 'bookings/services.html', {'categories': categories})


def home(request):
    services = SalonService.objects.select_related('category').all()
    return render(request, 'home.html', {'services': services})