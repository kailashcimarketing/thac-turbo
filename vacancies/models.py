from django.db import models
from wagtail.images.models import Image
from django_extensions.db.fields import AutoSlugField
from wagtail.documents.models import Document

# Create your models here.
class Category(models.Model):
    title = models.CharField(null=True,blank=False,max_length=255)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    
    def __str__(self):
        return self.title 

class Vacancies(models.Model):
    title = models.CharField(null=True,blank=False,max_length=500)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    start_date = models.DateField() 
    end_date = models.DateField()
    short_description = models.TextField()
    status = models.BooleanField(default=True,blank=True)
    weight = models.IntegerField(default=100,null=False,blank=False)
    document =  models.ForeignKey(
        Document,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    catgory = models.ForeignKey(
        'vacancies.category', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 

    def __str__(self):
        return self.title 