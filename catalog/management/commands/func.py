from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, fixture_path=None, *args, **options):
        categories_list = [
            {
                "id": 1,
                "name": "Электроника",
                "description": "Штучки, которые работают только при включении в сеть"
            },
            {
                "id": 2,
                "name": "Периферия",
                "description": "Штучки для компа"

            },
            {
                "id": 3,
                "name": "Прочее",
                "description": None
            }
        ]

        categories_for_create = []
        Category.objects.all().delete()
        for category_item in categories_list:
            categories_for_create.append(Category(**category_item))

        Category.objects.bulk_create(categories_for_create)

        products_list = [
            {
                "name": "Компьютерная мышка",
                "description": "Крутая, удобная",
                "image": "",
                "category": Category.objects.get(pk=2),
                "unit_price": 350,
                "create_date": "2025-03-15T17:47:41Z",
                "edit_date": "2025-03-15T17:47:42Z"
            },
            {
                "name": "Клавиатура",
                "description": "Беспроводная, механическая",
                "image": "",
                "category": Category.objects.get(pk=2),
                "unit_price": 2000,
                "create_date": "2025-03-15T17:48:05Z",
                "edit_date": "2025-03-15T17:48:07Z"
            },
            {
                "name": "Наушники",
                "description": "Такие себе, но пойдет",
                "image": "",
                "category": Category.objects.get(pk=2),
                "unit_price": 250,
                "create_date": "2025-03-15T17:48:28Z",
                "edit_date": "2025-03-15T17:48:29Z"
            },
            {
                "name": "Ноутбук",
                "description": "Классный",
                "image": "",
                "category": Category.objects.get(pk=1),
                "unit_price": 95000,
                "create_date": "2025-03-15T17:48:47Z",
                "edit_date": "2025-03-15T17:48:48Z"
            },
            {
                "name": "Настольная лампа",
                "description": "Ниче такая, пойдет",
                "image": "",
                "category": Category.objects.get(pk=1),
                "unit_price": 150,
                "create_date": "2025-03-15T17:49:12Z",
                "edit_date": "2025-03-15T17:49:13Z"
            }
        ]

        products_for_create = []
        Product.objects.all().delete()
        for product_item in products_list:
            products_for_create.append(Product(**product_item))

        Product.objects.bulk_create(products_for_create)
