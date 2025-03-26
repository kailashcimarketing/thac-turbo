from django.shortcuts import render, get_object_or_404
from pages.models import GeneralPage


def news_detail(request, slug):
    news_page = get_object_or_404(GeneralPage, slug='news-detail')
    return render(request, 'pages/news_detail.html', {"news_slug": slug, 'page': news_page})



def event_detail(request, slug):
    page = get_object_or_404(GeneralPage, slug='event-detail')
    return render(request, 'pages/event_detail.html', {"event_slug": slug, 'page': page})
