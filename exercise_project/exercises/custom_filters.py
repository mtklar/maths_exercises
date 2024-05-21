from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def preserve_whitespaces(text):
    return mark_safe(text.replace(" ", "&#32;").replace("\t", "&#9;"))
