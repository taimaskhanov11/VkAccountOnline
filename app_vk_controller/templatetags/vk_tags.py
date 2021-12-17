from pprint import pprint

from django import template
from django.urls import reverse

from app_vk_controller import db_peewee
from app_vk_controller.models import User, Account
from app_vk_controller.utils import get_weather_bar

register = template.Library()


@register.inclusion_tag('app_vk_controller/template_tags/weather_info.html')
def show_weather(request):
    # context = get_weather_bar(request)
    # return context
    return {
        'temperature': 12,
        'city': 'Махачкала',
        'country': 'Дагестан',
    }


@register.inclusion_tag('app_vk_controller/template_tags/last_message_info.html')
def show_last_messages():  # old
    # return
    context = {'data': db_peewee.Account.get_main_data()}
    # context = {}
    print(context)
    return context


@register.simple_tag
def get_status(obj):
    if isinstance(obj, Account):
        print(obj)
        if obj.blocked:
            return 'danger', 'Blocked'
        elif obj.start_status:
            return 'success', 'Active', 'warning', 'Приостановить',
        else:
            return 'warning', 'Stopped', 'success', 'Активировать',
    elif isinstance(obj, User):
        if obj.blocked:
            return 'danger', 'Blocked', 'success', 'Разблокировать'
        else:
            return 'success', 'Active', 'danger', 'Заблокировать'


@register.simple_tag
def get_all_accounts_and_users():
    context = {
        'users': User.objects.all(),
        'accounts': Account.objects.all()
    }

    return context


@register.inclusion_tag('app_vk_controller/template_tags/accounts_info.html')
def show_accounts():
    # return
    context = {'data': Account.get_main_data()}
    return context


@register.simple_tag
def get_range(x):
    return range(x)


@register.filter
def create_range(value, start_index=0):
    return range(start_index, value + start_index)
