from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from .models import NewsIndexPage

NewsIndexPage.content_panels = Page.content_panels + [
    FieldPanel('body'),
]
NewsIndexPage.promote_panels = Page.promote_panels + [
    FieldPanel('short_description'),
]