from django import template
from django.template import Template, Context
register = template.Library()
from events.models import Events, Category,EventCategory
from datetime import datetime
from django.utils import timezone
today = datetime.now()
from django.db.models import Exists, OuterRef

@register.simple_tag()
def get_event_categories():
    today = timezone.now().date()
    items = Category.objects.filter(
        Exists(
            Events.objects.filter(
                categories__category=OuterRef('pk'),
                release_date__lte=today,
                end_date__gte=today
            )
        )
    )
    return {'items': items}

@register.simple_tag()
def get_events():
    today = timezone.now().date()
    items = Events.objects.filter(
        status=True,
        end_date__gte=today,
        release_date__lte=today
    ).order_by('start_date')
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
