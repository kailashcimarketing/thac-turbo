from django.db import models
from wagtail.images.models import Image
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.models import ClusterableModel

class Category(models.Model):
    title = models.CharField(null=True,blank=False,max_length=255)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    
    def __str__(self):
        return self.title or "Unnamed Category"
    
class StaffCategory(models.Model):
    page = ParentalKey('Team', related_name='categories',null=True,blank=True)
    catgory = models.ForeignKey(
        'team.category', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+',
        verbose_name="Category"
    ) 
    panels = [
        # Use a SnippetChooserPanel because blog.BlogAuthor is registered as a snippet
        FieldPanel("catgory"),
    ]



# Create your models here.
class Team(ClusterableModel):
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
    panels = [
        FieldPanel('title'),
        FieldPanel('profile_picture'),
        #FieldPanel('catgory'),
        InlinePanel('categories', label='Categories', panels=[
            FieldPanel('catgory'),
        ]),
        FieldPanel('position'),
        FieldPanel('credentials'),
        FieldPanel('phone'),
        FieldPanel('status'),
        FieldPanel('weight'),
        FieldPanel('additional_information'),        
    ] 
    

    def __str__(self):
        return self.title or "Unnamed Team"

    class Meta:
        verbose_name = "Leadership Team"
        verbose_name_plural = "Leadership Team"

class TeamAbstract(models.Model):
    title = models.CharField(null=True,blank=False,max_length=255)
    profile_picture = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 
    position = models.CharField(null=True,blank=False,max_length=500)
    credentials = models.CharField(null=True,blank=True,max_length=500)
    phone = models.CharField(null=True,blank=True,max_length=50)
    email  = models.EmailField(null=True,blank=True)
    status = models.BooleanField(default=True,blank=True)
    weight = models.IntegerField(default=100,null=False,blank=False)
    additional_information = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

# Create your models here.
class Coaches(TeamAbstract,ClusterableModel):
    def __str__(self):
        return self.title or "Unnamed Team"

    class Meta:
        verbose_name = "Coach"
        verbose_name_plural = "Coaches"
         

class Tutors(TeamAbstract,ClusterableModel):
    def __str__(self):
        return self.title or "Unnamed Team"

    class Meta:
        verbose_name = "Tutor"                
        verbose_name_plural = "Tutors"


class Instructors(TeamAbstract,ClusterableModel):
    def __str__(self):
        return self.title or "Unnamed Team"

    class Meta:
        verbose_name = "Instructor"                
        verbose_name_plural = "Instructors"
