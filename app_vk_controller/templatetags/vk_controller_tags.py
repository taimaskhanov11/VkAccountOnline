from pprint import pprint

from django import template
from django.urls import reverse

register = template.Library()


def show_weather(categories, tags):
    pass