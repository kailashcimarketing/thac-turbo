from django import template
from django.template import Template, Context
register = template.Library()
from events.models import Events, Category,EventCategory
from datetime import datetime
from django.utils import timezone
today = datetime.now()

@register.simple_tag()
def get_event_categories():
    used_category_ids = EventCategory.objects.values_list('category_id', flat=True).distinct()
    # Filter categories using those IDs
    items = Category.objects.filter(id__in=used_category_ids).order_by('weight')
    return {'items':items}

@register.simple_tag()
def get_events():
    today = timezone.now().date()
    items = Events.objects.filter(status=True, end_date__gte=today).order_by('start_date')
    return {'items': items}

@register.simple_tag()
def get_homepage_featured_events():
    items = Events.objects.filter(homepage_featured_event=True)
    
    return {'items':items}

@register.simple_tag()
def get_event_detail(slug):
    try:
        detail = Events.objects.get(slug=slug)
    except Exception:
        detail = False
    return {
        'item': detail
    }
