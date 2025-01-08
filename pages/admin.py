from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from .models import GeneralPage,LandingPage

GeneralPage.content_panels = Page.content_panels + [
    InlinePanel('generalpage_hero', label='Hero Images', panels=[
        FieldPanel('image'),
        FieldPanel('background_video_url'),   
        FieldPanel('title'),
        FieldPanel('script_title'),
        FieldPanel('primary_tagline'),
        FieldPanel('secondary_tagline'),   
    ],max_num=1),
    FieldPanel('short_description'),
    FieldPanel('body'),
]


LandingPage.content_panels = Page.content_panels + [
    InlinePanel('landingpage_hero', label='Hero Images', panels=[
        FieldPanel('image'),
        #FieldPanel('title'),     
        FieldPanel('background_video_url'),   
    ],max_num=1),
    FieldPanel('body'),
]

