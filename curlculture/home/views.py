from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here you can save the email to your database or mailing list
        messages.success(request, "Thank you for subscribing!")
    return redirect(request.META.get('HTTP_REFERER', '/'))

def home_view(request):
    return render(request, 'home/home.html')
