from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

@login_required
def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_service.html', {'form': form})

def booking_confirmation(request):
    return render(request, 'bookings/booking_confirmation.html')
