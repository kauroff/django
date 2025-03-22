from django import template

register = template.Library()


# Создание тега
# @register.simple_tag
# def current_time(format_string):
#     return None


# Создание фильтра
@register.filter(needs_autoescape=True)
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'
