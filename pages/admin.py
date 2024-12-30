from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from .models import GeneralPage,LandingPage

GeneralPage.content_panels = Page.content_panels + [
    InlinePanel('generalpage_hero', label='Hero Images', panels=[
        FieldPanel('image'),
        FieldPanel('title'),        
    ],max_num=1),
    FieldPanel('body'),
]


LandingPage.content_panels = Page.content_panels + [
    InlinePanel('landingpage_hero', label='Hero Images', panels=[
        FieldPanel('image'),
        #FieldPanel('title'),     
        #FieldPanel('background_video_url'),   
    ],max_num=1),
    FieldPanel('body'),
]

