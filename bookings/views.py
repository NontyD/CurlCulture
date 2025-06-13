from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm, ContactForm
from django.contrib.auth.decorators import login_required
from .models import ServiceCategory, SalonService, Booking, ContactMessage
from django.contrib import messages


def services_view(request, category):
    """
    Display all services for a given category.
    """
    services = SalonService.objects.filter(category__name__iexact=category)
    return render(
        request,
        'bookings/services.html',
        {'services': services, 'category': category}
    )


@login_required
def book_service(request, service_id=None):
    """
    Handle booking for a specific service or show booking form.
    """
    service = get_object_or_404(SalonService, id=service_id) if service_id else None
    form = BookingForm(initial={'service': service}) if service else BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_confirmation')

    return render(
        request,
        'bookings/book_service.html',
        {'form': form, 'service': service}
    )


def booking_confirmation(request):
    """
    Show booking confirmation page.
    """

    return render(request, 'bookings/booking_confirmation.html')


def home(request):
    """
    Display all services on the home page.
    """
    services = SalonService.objects.select_related('category').all()
    return render(request, 'home.html', {'services': services})


def search(request):
    """
    Search for services by name.
    """
    query = request.GET.get('q')
    results = []
    if query:
        results = SalonService.objects.filter(name__icontains=query)
    return render(
        request,
        'bookings/search_results.html',
        {'results': results, 'query': query}
    )


def booking_detail(request, booking_id):
    """
    Display details for a specific booking.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})


def contact(request):
    """
    Handle contact form submissions.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'bookings/contact.html', {'form': form})
