from django.db import models
from wagtail.images.models import Image
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField, RichTextField
from pages.fields import events_stream_fields

class Category(models.Model):
    title = models.CharField(null=True,max_length=255,blank=False)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    weight = models.IntegerField(default=100,blank=False)    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"  # Correct plural form
        
    def __str__(self):
        return self.title

class EventCategory(Orderable):
    page = ParentalKey('Events', related_name='categories')
    category = models.ForeignKey('events.Category', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)



# Create your models here.
class Events(ClusterableModel):
    title = models.CharField(null=True,max_length=255,blank=False)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField()  
    release_date = models.DateField(null=True,blank=False,help_text="The date this event is intended to be publicly announced or made visible (for reference only; does not control visibility).")  
    time_label = models.CharField(null=True,blank=True,help_text='Overwrite the default event date label, e.g. Wednesday, 24th November, 1:00 PM – 5:15 PM.',verbose_name='Custom date label')  
    image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 
    hero_image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+',
        help_text='Detail page hero image'
    ) 
    short_description = models.TextField(null=True,blank=True)
    location = models.CharField(null=True,blank=True,max_length=255)
    status = models.BooleanField(default=True)
    homepage_featured_event = models.BooleanField(default=False,verbose_name="Show Featured Event on Homepage")
    promote = models.BooleanField(default=False,verbose_name="Promote")
    show_details = models.BooleanField(default=False,verbose_name="Show Details")
    button_label = models.CharField(null=True,blank=True,max_length=255)
    button_url = models.CharField(null=True,blank=True,max_length=255)    
    
    category = models.ForeignKey('events.Category', related_name='event_category', null=True, blank=True, on_delete=models.SET_NULL)
    weight = models.IntegerField(default=100,null=False,blank=False)
    body = StreamField(events_stream_fields,null=True,blank=True)

    def get_categories(self):
        if self.categories.all():
            return self.categories.all()
        
        return False
    
    def get_first_category(self):
        if self.get_categories():
            return self.get_categories()[0]
        
        return False
    
    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        FieldPanel('status'),
        FieldPanel('homepage_featured_event'),
        FieldPanel('promote'),
        FieldPanel('show_details'),
        FieldPanel('release_date'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('time_label'),
        FieldPanel('weight'),
        FieldPanel('image'),
        FieldPanel('hero_image'),
        FieldPanel('location'),
        FieldPanel('short_description'),
        FieldPanel('button_label'),
        FieldPanel('button_url'),
        InlinePanel('categories', label='Categories', panels=[
            FieldPanel('category'),
        ]),
        #FieldPanel('category'),        
        FieldPanel('body'),        
    ]
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Event'
