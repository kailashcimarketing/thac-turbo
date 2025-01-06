from django import template
from django.template import Template, Context
from django.utils.safestring import mark_safe
from vacancies.models import Vacancies, Category
register = template.Library()
from django.utils.timezone import now
today = now().date()

@register.simple_tag
def get_vacancies():
    items = Vacancies.objects.filter(end_date__gte=today, status=True)
    return {'items':items}

@register.simple_tag
def get_categories():
    items = Category.objects.all()
    return {'items':items}


