from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def discount(price):
    return int(price) * (100 - int(settings.DISCOUNT)) / 100