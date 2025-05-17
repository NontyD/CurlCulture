from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

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
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart_view')

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