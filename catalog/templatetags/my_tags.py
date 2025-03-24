from django import template

register = template.Library()


# Создание тега
@register.simple_tag
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'


# Создание фильтра
@register.filter
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'
