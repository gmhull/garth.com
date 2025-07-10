from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='to_ordered_list')
def to_ordered_list(value):
    lines = value.splitlines()
    list_items = [f'<li>{line.strip()}</li>' for line in lines if line.strip()]
    return mark_safe(f'<ol>{"".join(list_items)}</ol>')