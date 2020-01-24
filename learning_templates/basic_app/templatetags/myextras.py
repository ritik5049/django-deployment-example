from django import template

register = template.Library()

def cut(value,arg):
    # this cuts out all value of "arg" form string
    return value.replace(arg,'')

# register.filter('cut',cut)
# or
@register.filter(name='cut')
