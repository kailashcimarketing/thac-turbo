from django import template
from django.template import Template, Context
register = template.Library()
from events.models import Events, Category
from datetime import datetime

today = datetime.now()

@register.simple_tag()
def get_event_categories():
    items = Category.objects.all().order_by('weight')
    return {'items':items}

@register.simple_tag()
def get_events():
    items = Events.objects.filter(start_date__gte=today, status=True).order_by('start_date')
    
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
