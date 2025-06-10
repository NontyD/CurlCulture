from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem, Product
from .forms import CheckoutForm
from django.conf import settings
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
import json

def product_list(request):
    products = Product.objects.all()
    category = request.GET.get('category')
    sort = request.GET.get('sort')

    if category:
        products = products.filter(category__iexact=category)
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')

    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'shop/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': category,
        'selected_sort': sort,
    })

def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0
    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
        total += subtotal
    shipping = 0 if total > 30 else 5
    grand_total = total + shipping
    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'shipping': shipping,
        'grand_total': grand_total,
    })

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
    request.session['cart'] = cart
    request.session['just_added'] = product_id
    return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart_view')

def cart_added(request):
    product_id = request.session.pop('just_added', None)
    product = None
    if product_id:
        product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/cart_added.html', {'product': product})

def checkout_success(request):
    request.session['cart'] = {}
    return render(request, 'shop/checkout_success.html')


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_view')

    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0
    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
        total += subtotal
    shipping = 0 if total > 30 else 5
    grand_total = total + shipping

    stripe.api_key = settings.STRIPE_SECRET_KEY
    client_secret = None
    show_payment = False

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            metadata = {
                'user_id': str(request.user.id),
                'cart': json.dumps(cart)
            }
            intent = stripe.PaymentIntent.create(
                amount=int(grand_total * 100),
                currency='usd',
                receipt_email=form.cleaned_data['email'],
                metadata=metadata
            )
            client_secret = intent.client_secret
            show_payment = True  # Show Stripe payment form
    else:
        form = CheckoutForm()

    return render(request, 'shop/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'total': total,
        'shipping': shipping,
        'grand_total': grand_total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': client_secret,
        'show_payment': show_payment,
    })

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        email = payment_intent.get('receipt_email')
        metadata = payment_intent.get('metadata', {})
        user_id = metadata.get('user_id')
        cart_json = metadata.get('cart')
        try:
            user = User.objects.get(id=user_id)
            cart = json.loads(cart_json)
            products = Product.objects.filter(id__in=cart.keys())
            total = 0
            cart_items = []
            for product in products:
                quantity = cart[str(product.id)]
                subtotal = product.price * quantity
                cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
                total += subtotal
            shipping = 0 if total > 30 else 5
            grand_total = total + shipping

            # Prevent duplicate orders for the same PaymentIntent
            if not Order.objects.filter(user=user, total=grand_total, created_at__gte=timezone.now()-timezone.timedelta(minutes=10)).exists():
                order = Order.objects.create(
                    user=user,
                    total=grand_total,
                )
                for item in cart_items:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        quantity=item['quantity'],
                        price=item['product'].price,
                    )
                # Send confirmation email
                send_mail(
                    'Your CurlCulture Order Confirmation',
                    'Thank you for your order! Your payment was successful.',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
        except Exception as e:
            # Log error if needed
            pass

    return HttpResponse(status=200)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def product_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Product.objects.filter(name__icontains=query)
    return render(request, 'shop/product_search_results.html', {'results': results, 'query': query})