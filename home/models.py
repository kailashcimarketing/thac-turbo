from django.db import models

from wagtail.models import Page
from wagtail.images.models import Image
from pages.fields import homepage_stream_fields
from wagtail.fields import StreamField
from modelcluster.fields import ParentalKey
from wagtail.search import index

class SeoFieldsAbstract(models.Model):
    noindex = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="Exclude from Search Engines",
        help_text="Check this to prevent search engines from indexing this page (adds a 'noindex' meta tag)."
    ) 
    seo_image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+',
        verbose_name = 'Thumbnail for Social Sharing', 
        
    ) 
    
    class Meta:
        abstract = True

class HeroAbstract(models.Model):
    title = models.CharField(null=True,blank=True,max_length=255)
    script_title =models.CharField(null=True,blank=True,max_length=255) 
    primary_tagline = models.CharField(null=True,blank=True,max_length=255)
    secondary_tagline = models.CharField(null=True,blank=True,max_length=255)
    text = models.TextField(null=True,blank=True)
    image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 
    background_video_url = models.CharField(null=True,max_length=1000,blank=True,help_text="mp4 video",verbose_name="Background video")
    video_poster_image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    )
    popup_video_url = models.CharField(null=True,blank=True,help_text="",max_length=1000)
    button_label = models.CharField(null=True,blank=True,max_length=500)
    button_url = models.URLField(null=True,blank=True)

    class Meta:
        abstract = True

class HomepageHero(HeroAbstract):
    page = ParentalKey('HomePage', related_name='homepage_hero')

class HomePage(Page, SeoFieldsAbstract):
    body = StreamField(homepage_stream_fields, null=True, blank=True)

    search_fields = Page.search_fields + [ # Inherit search_fields from Page
        index.SearchField('body'),
        
    ]

    def get_hero(self):
        if self.homepage_hero.all():
            return self.homepage_hero.all()
        return False
        
