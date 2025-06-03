from django.db import models
from wagtail.images.models import Image
from django_extensions.db.fields import AutoSlugField
from wagtail.documents.models import Document
from django.utils.html import format_html
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    title = models.CharField(null=True,blank=False,max_length=255)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"  # Correct plural form

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
    
    class Meta:
        verbose_name = "Vacancies"
        verbose_name_plural = "Vacancies"  # Correct plural form

    def __str__(self):
        return self.title
    
    def status_icon(self):
        return format_html(
            '<span style="color:{};">{}</span>',
            'green' if self.status else 'red',
            'Active' if self.status else 'Inactive'
        )
    status_icon.short_description = 'Status'
    
    def lifecycle_status(self):
        today = now().date()
        if self.start_date and self.end_date and self.start_date > self.end_date:
            return format_html('<span style="color: red;">Invalid Dates</span>')
        elif self.start_date and today < self.start_date and self.status:
            return format_html('<span style="color: orange;">Scheduled</span>')
        elif self.end_date and today > self.end_date:
            return format_html('<span style="color: gray;">Expired</span>')
        elif self.status:
            return format_html('<span style="color: green;">Live</span>')
        else:
            return format_html('<span style="color: red;">Inactive</span>')
    lifecycle_status.short_description = 'Live Status'