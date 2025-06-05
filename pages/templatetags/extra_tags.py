import requests
from django import template
from django.conf import settings
from django.template import Template, Context
from pages.models import ContentHolder,LandingPage, PortalMenu
from django.utils.safestring import mark_safe
register = template.Library()
from news.models import Category,News,TopCategory
from django.utils.html import strip_spaces_between_tags, strip_tags
from datetime import datetime
import re
import random
today = datetime.now()

@register.filter
def is_booking_field(field):
    return field.name.startswith('booking_')

@register.filter
def not_booking_field(field):
    return not field.name.startswith('booking_')

@register.filter('klass')
def klass(ob):
    return ob.__class__.__name__

@register.filter
def highlight(string, term):
    max_length = 200
    parts = re.split(term, string, flags=re.IGNORECASE)
    lft = parts[0][len(parts[0]) - max_length:len(parts[0])]
    rht = '' if len(parts) < 2 else parts[1][:max_length]
    return mark_safe('...%s<b>%s</b>%s...' % (lft, term, rht))

@register.simple_tag()
def get_portal_links():
    return PortalMenu.objects.all().order_by('weight')

@register.inclusion_tag('pages/content-holders/content_holder.html',takes_context=True)
def load_content_holder(context, Slug):
    #try:
    header = ContentHolder.objects.get(slug=Slug)
    header = Template(header.content)
    html_header = header.render(context)
    #except Exception:
    #    html_header = "Content holder with name '" +Slug+"' not found."
    
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

@register.filter
def str_to_date(value, format="%Y-%m-%d"):
    try:
        return datetime.strptime(value, format).date()
    except (ValueError, TypeError):
        return None
    
@register.simple_tag()
def get_news_category():
    items = Category.objects.filter(newscategories__isnull=False).distinct()
    #print("---------------",items)
    return {'items':items}
@register.simple_tag()
def get_news_top_level_category():
    items = TopCategory.objects.distinct()
    #print("---------------",items)
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
        detail = News.objects.get(slug=slug)
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

@register.simple_tag
def get_news_items(category='all', limit='all'):
    if category != 'all':
        items = News.objects.filter(status=True,news_category__category__slug=category).order_by('-release_date')
    else:
        items = News.objects.filter(status=True).order_by('-release_date')

    if limit != 'all':
        try:
            limit = int(limit)
            items = items[:limit]
        except ValueError:
            pass  # fallback: return all items if limit is not an integer

    return {'items':items}

@register.simple_tag()
def get_next_pre_pages(page):
    if not page:
        return False

    # Get the current page's parent
    parent_page = page.specific.get_parent()

    # Get the previous page (sibling), published and in menu
    previous_page = (
        page.specific.get_prev_sibling()
        if page.specific.get_prev_sibling() and page.specific.get_prev_sibling().live and page.specific.get_prev_sibling().show_in_menus
        else None
    )

    # If no previous sibling, get the last child of the parent's previous sibling
    if not previous_page and parent_page.get_prev_sibling():
        previous_sibling = parent_page.get_prev_sibling()
        previous_page = (
            previous_sibling.get_children()
            .live()
            .in_menu()
            .last()
        )

    # Get the next page (sibling), published and in menu
    next_page = page.specific.get_next_sibling()
    if next_page and (not next_page.live or not next_page.show_in_menus):
        next_page = None

    # Try to get the second next page
    second_next_page = None
    if next_page:
        temp = next_page.get_next_sibling()
        if temp and temp.live and temp.show_in_menus:
            second_next_page = temp

    # If no next_page, get the first child of parent's next sibling
    if not next_page:
        next_sibling = parent_page.get_next_sibling()
        if next_sibling:
            next_page = (
                next_sibling.get_children()
                .live()
                .in_menu()
                .first()
            )
            # Attempt to get second next page after this
            if next_page:
                temp = next_page.get_next_sibling()
                if temp and temp.live and temp.show_in_menus:
                    second_next_page = temp

    # If second_next_page is still not found, try again from parent's next sibling
    if not second_next_page and parent_page.get_next_sibling():
        second_next_page = (
            parent_page.get_next_sibling()
            .get_children()
            .live()
            .in_menu()
            .first()
        )

    return {
        'previous_page': previous_page,
        'next_page': next_page,
        'second_next_page': second_next_page,
    }

@register.inclusion_tag('pages/content-holders/promo_title_image.html',takes_context=True)
def get_promo_section(context,page_slug):
        # Get the current page's parent
    try:
        page = LandingPage.objects.get(slug=page_slug).specific
        promo_title=page.specific.promo_title
    except Exception:
        promo_title = "Content holder with name '" +page_slug+"' not found."
    
    return {
            'promo_title': promo_title,
            'promo_image': page.specific.promo_image,
            'request': context['request'],  # To ensure images render correctly
    }

@register.filter
def is_mp4(url):
    return '.mp4' in url if url else False