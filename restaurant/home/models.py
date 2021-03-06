from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, FieldRowPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

# ----------------------
#   Site Wide Settings
# ----------------------
@register_setting
class RestaurantInfo(BaseSetting):
    site_name= models.TextField(blank=False)
    about = RichTextField()
    location = RichTextField()
    opening_times = RichTextField()

    # class Meta:
    #     verbose_name = "Restaurant Info"

# -------------------
#   HomePage Models
# -------------------

class HomePage(Page):
    template = 'home/home_page.pug'

    headline = models.TextField()
    intro = RichTextField()
    intro_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    specials = models.ForeignKey(
        'MenuSection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    reservation = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('intro'),
        ImageChooserPanel('intro_image'),
        SnippetChooserPanel('specials'),
        FieldPanel('reservation'),
    ]


# ---------------
#   Menu Models
# ---------------

class MenuItem(Orderable, models.Model):
    section = ParentalKey('MenuSection', related_name='menu_items')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    recommend = models.BooleanField()

    panels = [
        FieldPanel('name'),
        FieldRowPanel(children=[
            FieldPanel('price', classname='col8'),
            FieldPanel('recommend', classname='col4')
        ]),
        FieldPanel('description'),
    ]


@register_snippet
class MenuSection(ClusterableModel):
    name = models.CharField(max_length=100)

    panels = [
        FieldPanel('name'),
        MultiFieldPanel([
            InlinePanel('menu_items', min_num=1)
        ], heading='Add items')
    ]

    def __str__(self):
        return self.name

class MenuPageSectionPlacement(Orderable, models.Model):
    page = ParentalKey('MenuPage', related_name='section_placements')
    section = models.ForeignKey('MenuSection', related_name='+')

    class Meta:
        verbose_name = "section placement"
        verbose_name_plural = "section placements"

    panels = [
        SnippetChooserPanel('section'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.section.name


class MenuPage(Page):
    template = 'home/menu_page.pug'

    intro = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('section_placements', label='Sections'),
    ]
