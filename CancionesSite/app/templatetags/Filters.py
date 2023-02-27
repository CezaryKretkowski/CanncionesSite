from django import template

register = template.Library()

@register.filter(name='times') 
def times(number):
    return range(number)

@register.filter(name='dict_key')
def dict_key(d, k):
    return d[k]


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})