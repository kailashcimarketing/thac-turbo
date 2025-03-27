from django.db import models
from wagtail.images.models import Image
from django_extensions.db.fields import AutoSlugField

class Category(models.Model):
    title = models.CharField(null=True,blank=False,max_length=255)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    
    def __str__(self):
        return self.title 


# Create your models here.
class Team(models.Model):
    title = models.CharField(null=True,blank=False,max_length=255)
    profile_picture = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 
    catgory = models.ForeignKey(
        'team.category', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+',
        verbose_name="Category"
    ) 
    position = models.CharField(null=True,blank=False,max_length=500)
    credentials = models.CharField(null=True,blank=True,max_length=500)
    phone = models.CharField(null=True,blank=True,max_length=50)
    email  = models.EmailField(null=True,blank=True)
    status = models.BooleanField(default=True,blank=True)
    weight = models.IntegerField(default=100,null=False,blank=False)
    additional_information = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Team"