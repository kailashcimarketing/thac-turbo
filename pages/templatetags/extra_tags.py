from django import template
from django.template import Template, Context
from pages.models import ContentHolder
from django.utils.safestring import mark_safe
register = template.Library()
import re
import random

@register.filter
def highlight(string, term):
    max_length = 200
    parts = re.split(term, string, flags=re.IGNORECASE)
    lft = parts[0][len(parts[0]) - max_length:len(parts[0])]
    rht = '' if len(parts) < 2 else parts[1][:max_length]
    return mark_safe('...%s<b>%s</b>%s...' % (lft, term, rht))

@register.inclusion_tag('pages/content-holders/content_holder.html',takes_context=True)
def load_content_holder(context, Slug):
    try:
        header = ContentHolder.objects.get(slug=Slug)
        header = Template(header.content)
        html_header = header.render(context)
    except Exception:
        html_header = "Content holder with name '" +Slug+"' not found."
    
    return {
        'html_header': html_header
    }


