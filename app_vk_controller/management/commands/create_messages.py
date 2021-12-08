import datetime
from pprint import pprint

from django.core.management import BaseCommand

from app_vk_controller.models import Message, Account, User


class Command(BaseCommand):
    help = 'Добавить 1000 магазинов'

    def handle(self, *args, **options):
        account = Account.objects.get(id=1)
        user = User.objects.get(id=1)
        messages = [Message(account=account,
                            user=user,
                            text=str(i),
                            answer_question=str(i),
                            answer_template=str(i),
                            sent_at=datetime.datetime.now()
                            )
                    for i in range(1000)]
        Message.objects.bulk_create(messages)