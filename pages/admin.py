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
    FieldPanel('seo_image'),
    FieldPanel('noindex'),
]


LandingPage.content_panels = Page.content_panels + [
    FieldPanel('promo_page'),
    InlinePanel('landingpage_hero', label='Hero Images', panels=[
        FieldPanel('image'),
        FieldPanel('title'),     
        FieldPanel('background_video_url'),   
    ],max_num=1),
    FieldPanel('body'),
]
LandingPage.promote_panels = Page.promote_panels + [
    FieldPanel('short_description'),
    FieldPanel('seo_image'),
    FieldPanel('noindex'),
    #FieldPanel('promo_image'),
    #FieldPanel('promo_title'),
    #FieldPanel('promo_page'),    
]

EventPage.content_panels = Page.content_panels + [
    InlinePanel('eventpage_hero', label='Hero Images', panels=[
        FieldPanel('image'),
        FieldPanel('title'),     
        FieldPanel('script_title'),   
    ],max_num=1), 
    #FieldPanel('body'),
]

EventPage.promote_panels = Page.promote_panels + [
    FieldPanel('seo_image'),
    FieldPanel('noindex'),
]