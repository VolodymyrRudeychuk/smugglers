from django import template
from main_menu.models import Menu


register = template.Library()


@register.simple_tag
def menu(pre):
    menu_html = ''
    menu_o = Menu.objects.all()
    for item in menu_o:
        p = pre if '#' in item.url else ''
        menu_html += '<li><a class="page-scroll" href="%s%s">%s</a></li>' % (p, item.url, item.title)
    return menu_html


