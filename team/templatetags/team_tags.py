from django import template
from django.template import Template, Context
from django.utils.safestring import mark_safe
from team.models import Team, Category,Coaches, Tutors,Instructors, Boardmember
register = template.Library()
from django.utils.timezone import now
today = now().date()

@register.simple_tag
def get_coaches():
    items = Coaches.objects.filter(status=True).order_by('-weight')
    return {'items':items}

@register.simple_tag
def get_tutors():
    items = Tutors.objects.filter(status=True).order_by('-weight')
    return {'items':items}

@register.simple_tag
def get_instructors():
    items = Instructors.objects.filter(status=True).order_by('-weight')
    return {'items':items}

@register.simple_tag
def get_boardmembers():
    items = Boardmember.objects.filter(status=True).order_by('-weight')
    return {'items':items}

@register.simple_tag
def get_team(**kwargs):
    category = kwargs.get('category', 'all')
    limit = kwargs.get('limit', 'all')
    exclude_item = kwargs.get('exclude_item', False)
    
    if not category == 'all':
        items = Team.objects.filter(status=True,categories__catgory__slug=category)
    else:
        items = Team.objects.filter(status=True)

    if exclude_item:
        items = items.exclude(categories__catgory__slug=exclude_item)
    items = items.order_by('-weight')
    if limit != 'all':
        try:
            limit = int(limit)
            items = items[:limit]
        except ValueError:
            pass  # fallback: return all items if limit is not an integer
        
    return {'items':items}

@register.simple_tag
def get_categories(exclude_item=False):
    items = Category.objects.all().order_by('-weight')
    if exclude_item:
        items = items.exclude(slug=exclude_item)
    return {'items':items}


