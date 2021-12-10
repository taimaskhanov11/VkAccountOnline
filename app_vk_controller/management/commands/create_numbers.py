import datetime
from pprint import pprint

from django.core.management import BaseCommand

from app_vk_controller.models import Message, Account, User, Number


class Command(BaseCommand):
    help = 'Добавить 1000 магазинов'

    def handle(self, *args, **options):
        account = Account.objects.get(id=1)
        user = User.objects.get(id=1)
        messages = [Number(account=account,
                           user=user,
                           number=str(i)
                           )
                    for i in range(100)]
        Number.objects.bulk_create(messages)
