from django.db import models
from wagtail.images.models import Image
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from home.models import HeroAbstract
from pages.fields import generalpage_stream_fields
from wagtail.fields import StreamField, RichTextField

class Category(models.Model):
    title = models.CharField(null=True,max_length=255,blank=False)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    weight = models.IntegerField(default=100,blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Category'

class NewsCategories(Orderable):   
    category = models.ForeignKey(
        "news.Category",
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    page = ParentalKey('News', related_name='news_category')
  

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
    published_date = models.DateField()
    status = models.BooleanField(default=True)
    
    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        FieldPanel('image'),
        FieldPanel('short_description'),
        FieldPanel('published_date'),
        FieldPanel('status'),
        InlinePanel('news_category', label='Categories', panels=[
            FieldPanel('category'),
        ],max_num=1),
        

    ]
    class Meta:
        verbose_name = 'News'


class NewspageHero(HeroAbstract):
    page = ParentalKey('NewsIndexPage', related_name='newspage_hero')

class NewsIndexPage(Page):
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