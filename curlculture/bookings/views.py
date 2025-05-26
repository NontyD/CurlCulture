from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from .models import ServiceCategory, SalonService, Booking


def services_view(request, category):
    # Fetch services for the selected category
    services = SalonService.objects.filter(category__name__iexact=category)
    return render(request, 'bookings/services.html', {'services': services, 'category': category})

@login_required
def book_service(request, service_id=None):
    # Handle booking for a specific service
    service = get_object_or_404(SalonService, id=service_id) if service_id else None
    form = BookingForm(initial={'service': service}) if service else BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_confirmation')

    return render(request, 'bookings/book_service.html', {'form': form, 'service': service})


def booking_confirmation(request):
    return render(request, 'bookings/booking_confirmation.html')



def home(request):
    services = SalonService.objects.select_related('category').all()
    return render(request, 'home.html', {'services': services})


def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = SalonService.objects.filter(name__icontains=query)
    return render(request, 'bookings/search_results.html', {'results': results, 'query': query})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})