from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import CheckoutForm
from django.conf import settings
import stripe

# Product list with optional filtering and sorting
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

# Cart view
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
    shipping = 0 if total > 30 else 5  # Free shipping over $30
    grand_total = total + shipping
    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'shipping': shipping,
        'grand_total': grand_total,
    })

# Add to cart
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
    request.session['cart'] = cart
    request.session['just_added'] = product_id
    return redirect('cart_view')

# Remove from cart
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart_view')

# Cart added feedback (not used if you redirect straight to cart)
def cart_added(request):
    product_id = request.session.pop('just_added', None)
    product = None
    if product_id:
        product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/cart_added.html', {'product': product})

# Checkout with Stripe Elements (embedded payment)
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

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create Stripe PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=int(grand_total * 100),  # Stripe expects cents
                currency='usd',
                receipt_email=form.cleaned_data['email'],
            )
            client_secret = intent.client_secret
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
    })

# Checkout success page
def checkout_success(request):
    request.session['cart'] = {}
    return render(request, 'shop/checkout_success.html')