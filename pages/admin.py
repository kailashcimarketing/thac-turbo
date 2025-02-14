from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from .models import GeneralPage,LandingPage, EventPage

GeneralPage.content_panels = Page.content_panels + [
    InlinePanel('generalpage_hero', label='Hero Images', panels=[
        FieldPanel('image'),
        FieldPanel('background_video_url'),   
        FieldPanel('title'),
        FieldPanel('script_title'),
        FieldPanel('primary_tagline'),
        FieldPanel('secondary_tagline'),   
    ],max_num=1),
    FieldPanel('body'),
]
GeneralPage.promote_panels = Page.promote_panels + [
    FieldPanel('short_description'),
]


LandingPage.content_panels = Page.content_panels + [
    InlinePanel('landingpage_hero', label='Hero Images', panels=[
        FieldPanel('image'),
        FieldPanel('title'),     
        FieldPanel('background_video_url'),   
    ],max_num=1),
    FieldPanel('body'),
]


EventPage.content_panels = Page.content_panels + [
    FieldPanel('hero_image'),
    FieldPanel('hero_title'),     
    FieldPanel('hero_script_title'),   
    #FieldPanel('body'),
]