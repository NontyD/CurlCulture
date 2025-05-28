from django.contrib.auth.models import User
from django.contrib.auth import logout, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from shop.models import Order

@login_required
def profile(request):
    user_bookings = Booking.objects.filter(user=request.user)
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'accounts/profile.html', {
        'bookings': user_bookings,
        'orders': user_orders,
    })
    
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until it is confirmed
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your CurlCulture Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail(subject, message, 'noreply@curlculture.com', [user.email])
            return render(request, 'registration/activation_sent.html')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration/activation_complete.html')
    else:
        return render(request, 'registration/activation_invalid.html')
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')
    return render(request, 'accounts/delete_account.html')