from home.models import MenuSection, MenuPageSectionPlacement
from django import template

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page

@register.inclusion_tag('home/tags/menu_sections.pug', takes_context=True)
def section_placements(context, page):
    return {
        'section_placements': MenuPageSectionPlacement.objects.filter(page = page),
        'request': context['request'],
    }

# Single menu section – used for HomePage specials
@register.inclusion_tag('home/tags/menu_section.pug', takes_context=True)
def menu_section(context, id):
    return {
        'menu_section': MenuSection.objects.filter(id = id),
        'request': context['request'],
    }

# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('home/tags/top_menu.pug', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().filter(
        live=True,
        show_in_menus=True
    )
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
