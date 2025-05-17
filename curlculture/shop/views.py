from django.shortcuts import render
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