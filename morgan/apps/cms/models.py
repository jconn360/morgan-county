from django.db import models
from django.utils.translation import ugettext as _

from wagtail.wagtailsearch import index
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):

    video = models.URLField(
        _('Background Video'),
        null=True
    )

    def __unicode__(self):
        return self.title

    subpage_types = ['cms.Offices']
    content_panels = [
        FieldPanel('title'),
        FieldPanel('video'),
    ]

class Offices(Page):

    def __unicode__(self):
        return self.title

    subpage_types = ['cms.Office']
    content_panels = [
        FieldPanel('title'),
    ]

class Office(Page):

    official = models.CharField(
        _('Official\'s Name'),
        max_length=30,
        null=True,
    )
    phone = models.CharField(
        _('Phone'),
        max_length=15,
        null=True,
    )
    portrait = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Portrait'),
        null=True,
        on_delete=models.SET_NULL,
    )
    address = models.TextField(
        _('Address'),
        null=True,
    )
    body = models.TextField(
        _('Page Body'),
        null=True,
    )

    subpage_types = ['cms.OfficePage']
    content_panels = [
        FieldPanel('title'),
        FieldPanel('official'),
        FieldPanel('phone'),
        ImageChooserPanel('portrait'),
        FieldPanel('address'),
        FieldPanel('body'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('official'),
        index.SearchField('body'),
    )


class OfficePage(Page):

    body = models.TextField(
        _('Page Body'),
        null=True,
    )

    subpage_types = []
    content_panels = [
        FieldPanel('title'),
        FieldPanel('body'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

