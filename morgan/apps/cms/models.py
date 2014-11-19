from django.db import models
from django.utils.translation import ugettext as _

from modelcluster.fields import ParentalKey
from wagtail.wagtailsearch import index
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField


class ImageSlideshow(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Image'),
        null=True,
        on_delete=models.SET_NULL,
    )
    attribution = models.CharField(
        _('Attribution Link'),
        max_length=255,
        null=True,
        blank=True,
    )
    author = models.CharField(
        _('Author'),
        max_length=50,
        null=True,
        blank=True,
    )

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('attribution'),
        FieldPanel('author'),
    ]


class HomePageImageSlideshow(ImageSlideshow):
    page = ParentalKey('cms.HomePage', related_name='image_slideshow')

class HomePage(Page):

    def __unicode__(self):
        return self.title

    subpage_types = ['cms.Offices']

HomePage.content_panels = [
    FieldPanel('title'),
    InlinePanel(HomePage, 'image_slideshow', label='Image Slideshow'),
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
    email = models.CharField(
        _('Email'),
        help_text='(Optional)',
        max_length=255,
        null=True,
        blank=True,
    )
    fax = models.CharField(
        _('Fax'),
        help_text='(Optional)',
        max_length=15,
        null=True,
        blank=True,
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

    subpage_types = ['cms.OfficePage', 'cms.FormPage']
    content_panels = [
        FieldPanel('title'),
        FieldPanel('official'),
        FieldPanel('phone'),
        FieldPanel('email'),
        FieldPanel('fax'),
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


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')

class FormPage(AbstractEmailForm):
    body = models.TextField(_('Introduction'))
    success = models.CharField(
        _('Success Message'),
        max_length=255,
        help_text='This message is shown after the form is submitted.',
    )

    subpage_types = []
    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

FormPage.content_panels = [
    FieldPanel('title'),
    FieldPanel('body', classname="full"),
    FieldPanel('success'),
    MultiFieldPanel([
        FieldPanel('to_address'),
        FieldPanel('from_address'),
        FieldPanel('subject'),
    ], 'Email'),
    InlinePanel(FormPage, 'form_fields', label='Form fields'),
]

