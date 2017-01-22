from home.models import MenuSection, MenuPageSectionPlacement
from django import template

register = template.Library()

@register.inclusion_tag('home/tags/menu_sections.html', takes_context=True)
def section_placements(context):
    return {
        'section_placements': MenuPageSectionPlacement.objects.all(),
        'request': context['request'],
    }
