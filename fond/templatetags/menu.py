from django import template
from fond.models import Vcontrol
from sobstvenikam.models import Sobstvenikam

register = template.Library()


@register.inclusion_tag('tags/menu-tag.html')
def fond_menu():
    return {
        'control': Vcontrol.objects.all()}


@register.inclusion_tag('tags/menu-sob.html')
def menu_sob():
    return {
        'sob': Sobstvenikam.objects.all()}
