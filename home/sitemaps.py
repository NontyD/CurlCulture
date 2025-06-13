from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home', 'shop', 'contact', 'reviews']  # Add your named URLs

    def location(self, item):
        return reverse(item)
