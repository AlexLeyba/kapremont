from django import template

from fond.models import CategoryFond, CeoFond

register = template.Library()


@register.inclusion_tag('tags/menu-tag.html')
def fond_menu():
    return {"fond": CategoryFond.objects.all(),
            'ceo': CeoFond.objects.all()}
