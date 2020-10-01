from django import template

register = template.Library()

"""
Usage : {{ value|module:by }}

"""


@register.filter(name='modulo')
def modulo(value, by):
    return value % by
