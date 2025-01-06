from django import template
from django.template import Template, Context
from django.utils.safestring import mark_safe
from team.models import Team, Category
register = template.Library()
from django.utils.timezone import now
today = now().date()

@register.simple_tag
def get_team():
    items = Team.objects.filter(status=True)
    return {'items':items}

@register.simple_tag
def get_categories():
    items = Category.objects.all()
    return {'items':items}


