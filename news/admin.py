from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from .models import NewsIndexPage

NewsIndexPage.content_panels = Page.content_panels + [
    InlinePanel('newspage_hero', label='Hero Images', panels=[
        FieldPanel('image'),
        FieldPanel('title'),
    ],max_num=1),
    FieldPanel('body'),
]
NewsIndexPage.promote_panels = Page.promote_panels + [
    FieldPanel('short_description'),
    FieldPanel('seo_image'),
    FieldPanel('noindex'),
]