from django import template
from django.template import Template, Context
from django.utils.safestring import mark_safe
from team.models import Team, Category
register = template.Library()
from django.utils.timezone import now
today = now().date()

@register.simple_tag
def get_team(category='all',limit='all'):
    if not category == 'all':
        items = Team.objects.filter(status=True,catgory__slug=category)
    else:
        items = Team.objects.filter(status=True)
        
    if limit != 'all':
        try:
            limit = int(limit)
            items = items[:limit]
        except ValueError:
            pass  # fallback: return all items if limit is not an integer
        
    return {'items':items}

@register.simple_tag
def get_categories():
    items = Category.objects.all()
    return {'items':items}


