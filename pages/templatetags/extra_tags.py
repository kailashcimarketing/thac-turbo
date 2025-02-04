import requests
from django import template
from django.conf import settings
from django.template import Template, Context
from pages.models import ContentHolder
from django.utils.safestring import mark_safe
register = template.Library()
from news.models import NewsCategories
from django.utils.html import strip_spaces_between_tags, strip_tags
from datetime import datetime
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
@register.filter
def rm_tags(string,tags):
    html = string
    pattern = r'<[ ]*style.*?\/[ ]*style[ ]*>'  # mach any char zero or more times
    text = re.sub(pattern, '', html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
    text = strip_tags(text)
    return text

@register.simple_tag()
def get_news_category():
    items = NewsCategories.objects.all()
    return {'items':items}

@register.simple_tag()
def get_news_list(category='all',limit='all', ):
    today = datetime.today().strftime('%Y-%m-%d')
    featured_item = False
    try:
        news_items = []
        try:
            if category != 'all':
                r = requests.get(settings.NEWS_URL+'?category='+category,verify=False,timeout=settings.NEWS_REQUEST_TIMEOUT)
            else:
                r = requests.get(settings.NEWS_URL,verify=False,timeout=settings.NEWS_REQUEST_TIMEOUT)

        except ReadTimeout:
            return {'items':news_items}

        if r.status_code == 200:
            items = r.json()
            for item in items.get('results'):
                if item.get('release_date') != "None" and item.get('release_date'):
                    valid_news = True
                    
                    if valid_news:
                        if item.get('release_date'):
                            if today >= item.get('release_date'):
                                items['release_date'] = datetime.strptime(item.get('release_date'), "%Y-%m-%d").date()
                                news_items.append(item)  
                    
                    if item.get('featured') and featured_item == False:
                            featured_item = item
            
            if limit != 'all':
                news_items = news_items[:limit]            

    except Exception:
        items = []

    return {
        'items': news_items,
        'featured_item':featured_item,
    }    

@register.simple_tag()
def get_news_detail(slug):
    try:
        detail = False
        try:
            r = requests.get(settings.NEWS_URL,verify=False,timeout=settings.NEWS_REQUEST_TIMEOUT)
        except ReadTimeout:
            return {'item':False}

        if r.status_code == 200:
            full_json = r.json()
            if full_json:
                for item in full_json.get('results'):
                    if slug == item.get("slug"):
                        detail = item
                        break
    except Exception:
        detail = False
    return {
        'item': detail
    }  


@register.simple_tag()
def get_related_news(category='all', limit='all',related='all'):
    today = datetime.today().strftime('%Y-%m-%d')
    try:
        news_items = []
        try:
            if category != 'all':
                r = requests.get(settings.NEWS_URL+'?category='+category,verify=False,timeout=settings.NEWS_REQUEST_TIMEOUT)
            else:
                r = requests.get(settings.NEWS_URL,verify=False,timeout=settings.NEWS_REQUEST_TIMEOUT)

        except ReadTimeout:
            return {'items':news_items}

        if r.status_code == 200:
            items = r.json()
            for item in items.get('results'):
                if item.get('release_date') != "None" and item.get('release_date'):
                    valid_news = True
                    
                    if valid_news:
                        if item.get('release_date'):
                            if item.get('title') != related and today >= item.get('release_date'):
                                news_items.append(item)  
            
            if limit != 'all':
                news_items = news_items[:limit]            

    except Exception:
        items = []

    return {
        'items': news_items,
    }  



