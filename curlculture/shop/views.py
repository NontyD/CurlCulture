from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
import stripe
from django.conf import settings

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
    shipping = 0 if total > 30 else 5  # Free shipping over $30
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
    request.session['just_added'] = product_id  # For feedback modal
    return redirect('cart_added')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart_view')

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_view')
    # Here you would process payment and order creation
    # For now, just clear the cart and show a confirmation
    request.session['cart'] = {}
    return render(request, 'shop/checkout_success.html')

def cart_added(request):
    product_id = request.session.pop('just_added', None)
    product = None
    if product_id:
        product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/cart_added.html', {'product': product})

# Add Stripe configuration
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_view')

    products = Product.objects.filter(id__in=cart.keys())
    line_items = []
    total = 0
    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        total += subtotal
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100),  # Stripe expects cents
            },
            'quantity': quantity,
        })

    shipping = 0 if total > 30 else 500  # in cents
    if shipping > 0:
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': 'Shipping'},
                'unit_amount': shipping,
            },
            'quantity': 1,
        })

    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/shop/checkout/success/'),
        cancel_url=request.build_absolute_uri('/shop/cart/'),
    )
    return redirect(session.url, code=303)

def checkout_success(request):
    # Optionally clear the cart
    request.session['cart'] = {}
    return render(request, 'shop/checkout_success.html')