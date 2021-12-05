from pprint import pprint

from django.core.management import BaseCommand

from app_vk_controller.models import Account


class Command(BaseCommand):
    help = 'Добавить 1000 магазинов'

    def handle(self, *args, **options):

        # pprint(Account.objects.first()._meta.local_fields)
        pprint(Account.objects.first().__dict__ )

        self.stdout.write('Успешно удалены!')
