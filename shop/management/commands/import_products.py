import json
from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = 'Import products from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs['json_file'], 'r') as f:
            data = json.load(f)
            for item in data:
                Product.objects.update_or_create(
                    name=item['name'],
                    defaults={
                        'description': item['description'],
                        'price': item['price'],
                        'category': item['category'],
                        'image': item.get('image', ''),
                        'in_stock': item.get('in_stock', True),
                    }
                )
        self.stdout.write(self.style.SUCCESS('Products imported successfully!'))