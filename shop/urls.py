from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
    path('cart-added/', views.cart_added, name='cart_added'),
    path('stripe/webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('product-search/', views.product_search, name='product_search'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]