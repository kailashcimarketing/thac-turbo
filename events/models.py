from django.db import models
from wagtail.images.models import Image
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

class Category(models.Model):
    title = models.CharField(null=True,max_length=255,blank=False)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    weight = models.IntegerField(default=100,blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Category'


# Create your models here.
class Events(ClusterableModel):
    title = models.CharField(null=True,max_length=255,blank=False)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()    
    image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 
    short_description = models.TextField(null=True,blank=True)
    published_date = models.DateField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey('events.Category', related_name='event_category', null=True, blank=True, on_delete=models.SET_NULL)
    
    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('image'),
        FieldPanel('short_description'),
        FieldPanel('category'),
        FieldPanel('status'),
        
    ]
    class Meta:
        verbose_name = 'News'
