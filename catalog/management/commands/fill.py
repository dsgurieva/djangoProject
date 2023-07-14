from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_list = [
            {'name': 'фрукты', 'description': 'сезонные'},
            {'name': 'овощи', 'description': 'сезонные'},
            {'name': 'крупы', 'description': 'сезонные'},
            {'name': 'орехи', 'description': 'сезонные'},
        ]

        category_create = []
        for categori in category_list:
            category_create.append(
                Category(**categori)
            )

        Category.objects.bulk_create(category_create)



