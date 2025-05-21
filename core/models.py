from django.db import models
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.images.models import Image

@register_setting
class ExtraStyleSettings(BaseSiteSetting):
    extra_css = models.TextField("CSS Overrides", blank=True)
    extra_js = models.TextField("JavaScript Overrides", blank=True)

    class Meta:
        verbose_name = "Global CSS/JS"
        verbose_name_plural = "Global CSS/JS"


@register_setting
class GlobalAnnouncement(BaseSiteSetting):
    status = models.BooleanField(default=False,blank=True,help_text="Check to show alert message",verbose_name="Enable Popup")
    title = models.CharField(null=True,blank=False,max_length=255)
    date_label = models.CharField(null=True,blank=False,max_length=255,verbose_name='Date and Time label')
    text = models.TextField(null=True,blank=True)
    button_label = models.CharField(null=True,blank=True,max_length=255) 
    button_url = models.URLField(null=True,blank=True)
    tagline = models.CharField(null=True,blank=True,max_length=255)
    
    class Meta:
        verbose_name = "Global Announcement"
        verbose_name_plural = "Global Announcement"        


@register_setting
class AdminSettings(BaseSiteSetting):
    admin_logo = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 

    class Meta:
        verbose_name = "Admin Setting"
        verbose_name_plural = "Admin Settings"        