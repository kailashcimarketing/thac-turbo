from wagtail.admin.panels import FieldPanel, InlinePanel

from .models import HomePage

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
