from itertools import chain
from django import template

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page

@register.inclusion_tag('tags/main_menu.html', takes_context=True)
def main_menu(context, parent, calling_page=None):
    menu_items = parent.get_children().filter(live=True, show_in_menus=True)
    return {
        'calling_page': calling_page,
        'menu_items': list(chain([parent], menu_items)),
        'request': context['request'],
    }

