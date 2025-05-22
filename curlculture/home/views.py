from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import ContactForm

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here you can save the email to your database or mailing list
        messages.success(request, "Thank you for subscribing!")
    return redirect(request.META.get('HTTP_REFERER', '/'))

def home_view(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you can send an email or save the message
            messages.success(request, "Thank you for contacting us! We'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})

def privacy_policy(request):
    return render(request, 'privacy_policy.html')