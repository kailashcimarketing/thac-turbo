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
    status = models.BooleanField(default=False,blank=True,help_text="Check to show alert message",verbose_name="Show alert")
    text = RichTextField(blank=True,null=True,verbose_name="Text")
    
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