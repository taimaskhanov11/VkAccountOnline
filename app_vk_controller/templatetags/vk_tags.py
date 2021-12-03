from pprint import pprint

from django import template
from django.urls import reverse

from app_vk_controller.db_peewee import Account
from app_vk_controller.models import User
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
def show_last_messages():
    # return
    context = {'data': Account.get_main_data()}
    return context


@register.simple_tag
def get_status(obj):
    print(obj)
    if isinstance(obj,Account):
        if obj.blocked:
            return ('danger', 'Blocked')
        elif obj.start_status:
            return ('success', 'Active')
        else:
            return ('warning', 'Stopped')
    elif isinstance(obj,User, ):
        if obj.blocked:
            return ('danger', 'Blocked')
        else:
            return ('success', 'Active')


@register.simple_tag
def get_object_dict(obj):
    return obj.__dict__


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
