from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import SubscribeForm
from bookings.forms import ContactForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have subscribed to the newsletter!")
            return redirect('subscribe')
    else:
        form = SubscribeForm()
    return render(request, 'home/subscribe.html', {'form': form})


def home_view(request):
    return render(request, 'home/home.html')


def contact(request):
    """
    Handle contact form submissions on the home page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # You can send an email or save the message here if needed
            messages.success(
                request,
                "Thank you for contacting us! We'll get back to you soon."
            )
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})


def privacy_policy(request):
    return render(request, 'privacy_policy.html')