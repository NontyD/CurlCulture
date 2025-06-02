"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views as home_views
from bookings import views as bookings_views
from accounts import views as accounts_views
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/', bookings_views.contact, name='contact'),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # For built-in auth views
    path('accounts/', include('accounts.urls')), 
    path('subscribe/', home_views.subscribe, name='subscribe'),
    path('reviews/', include('reviews.urls')),
    path('shop/', include('shop.urls')),
    path('', include('home.urls')),
    path('privacy-policy/', home_views.privacy_policy, name='privacy_policy'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    ]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)