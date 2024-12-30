from django.db import models

from wagtail.models import Page
from wagtail.images.models import Image
from pages.fields import homepage_stream_fields
from wagtail.fields import StreamField
from modelcluster.fields import ParentalKey

class HeroAbstract(models.Model):
    title = models.CharField(null=True,blank=True,max_length=255)
    script_title =models.CharField(null=True,blank=True,max_length=255) 
    text = models.TextField(null=True,blank=True)
    image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 
    background_video_url = models.URLField(null=True,blank=True,help_text="mp4 video",verbose_name="Mp4 Video")
    video_poster_image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    )
    popup_video_url = models.URLField(null=True,blank=True,help_text="embeded video url")
    button_label = models.CharField(null=True,blank=True,max_length=500)
    button_url = models.URLField(null=True,blank=True)

    class Meta:
        abstract = True

class HomepageHero(HeroAbstract):
    page = ParentalKey('HomePage', related_name='homepage_hero')

class HomePage(Page):
    body = StreamField(homepage_stream_fields, null=True, blank=True)

    def get_hero(self):
        if self.homepage_hero.all():
            return self.homepage_hero.all()
        return False
        
