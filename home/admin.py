from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from .models import HomePage,Custom404Page

HomePage.content_panels = [
    FieldPanel('title', classname='title'),
    InlinePanel('homepage_hero', label='Hero Images', panels=[        
        FieldPanel('title'), 
        FieldPanel('script_title'),
        FieldPanel('image'),
        FieldPanel('background_video_url'),
        FieldPanel('video_poster_image'),
        FieldPanel('popup_video_url'),
        FieldPanel('button_label'), 
        FieldPanel('button_url'),  
        #FieldPanel('popup_video_url'),
    ],max_num=1),
    FieldPanel('body'),
]


HomePage.promote_panels = HomePage.promote_panels+[
    FieldPanel('seo_image'),
    FieldPanel('noindex'),
]

Custom404Page.content_panels = Page.content_panels + [
    InlinePanel('custom404_page_hero', label='Hero Images', panels=[
        FieldPanel('image'),
        FieldPanel('background_video_url'),   
        FieldPanel('title'),
        FieldPanel('script_title'),
        FieldPanel('primary_tagline'),
        FieldPanel('secondary_tagline'),   
    ],max_num=1),
    FieldPanel('body'),
]
Custom404Page.promote_panels = Page.promote_panels + [
    #FieldPanel('short_description'),
    #FieldPanel('seo_image'),
    FieldPanel('noindex'),
]
