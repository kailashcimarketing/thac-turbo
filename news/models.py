from django.db import models
from wagtail.images.models import Image
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, MultipleChooserPanel
from home.models import HeroAbstract, SeoFieldsAbstract
from pages.fields import generalpage_stream_fields,newspage_stream_fields
from wagtail.fields import StreamField, RichTextField

class Category(models.Model):
    title = models.CharField(null=True,max_length=255,blank=False)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    weight = models.IntegerField(default=100,blank=False)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"  # Correct plural form

    def __str__(self):
        return self.title
    
class TopCategory(models.Model):
    title = models.CharField(null=True,max_length=255,blank=False)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    weight = models.IntegerField(default=100,blank=False)
    
    class Meta:
        verbose_name = "Top Level Category"
        verbose_name_plural = "Top Level Categories"  # Correct plural form

    def __str__(self):
        return self.title


class NewsCategories(Orderable):   
    category = models.ForeignKey(
        "news.Category",
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    page = ParentalKey('News', related_name='news_category')
    
class NewsTopCategories(Orderable):   
    category = models.ForeignKey(
        "news.TopCategory",
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    page = ParentalKey('News', related_name='top_news_category')
  

# Create your models here.
class News(ClusterableModel):
    title = models.CharField(null=True,max_length=255,blank=False)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 
    short_description = models.TextField(null=True,blank=True)
    release_date = models.DateField()
    status = models.BooleanField(default=True)
    body = StreamField(newspage_stream_fields,null=True,blank=True)
    
    def get_photogallery(self):
        if self.gallery_images.all():
            return self.gallery_images.all()
        
        return False

    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        FieldPanel('image'),
        FieldPanel('short_description'),
        FieldPanel('release_date'),
        FieldPanel('status'),
        InlinePanel('top_news_category', label='Top level Categories', panels=[
            FieldPanel('category'),
        ]),
        InlinePanel('news_category', label='Categories', panels=[
            FieldPanel('category'),
        ]),
        
        MultipleChooserPanel(
            'gallery_images', label="Gallery images", chooser_field_name="image"
        ),
        FieldPanel('body'),
        

    ]
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

class NewsGalleryImage(Orderable):
    page = ParentalKey(News, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class NewspageHero(HeroAbstract):
    page = ParentalKey('NewsIndexPage', related_name='newspage_hero')

class NewsIndexPage(Page, SeoFieldsAbstract):
    short_description = models.TextField(null=True,blank=True)
    body = StreamField(generalpage_stream_fields,null=True,blank=True)
    """
    We'll render news items from SendHQ with JSON.
    """
    template = 'pages/news_index.html'
    class Meta:
        verbose_name = "News Index Page"

    def get_hero_image(self):
        if self.get_hero():
            return self.get_hero()[0]
        
        return False
        

    def get_hero(self):
        if self.newspage_hero.all():
            return self.newspage_hero.all()
        else:
            return False