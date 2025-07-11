from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from pages import views as pages_views

from search import views as search_views
from wagtail.images.views.serve import ServeView

from wagtail.models import Site
from home.models import Custom404Page
from django.shortcuts import render




urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path('news/<slug:slug>/', pages_views.news_detail, name='news_detail_page'),
    path('events/<slug:slug>/', pages_views.event_detail, name='event_detail_page'),
    path('profile/<slug:slug>/',pages_views.profile_detail,name='profile_detail'),
    re_path(r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(), name='wagtailimages_serve'),
    path("robots.txt", include("robots.urls")),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]

def wagtail_custom_404(request, exception):
    site = Site.find_for_request(request)
    try:
        error_page = Custom404Page.objects.live().descendant_of(site.root_page).first()
        if error_page:
            return render(request, error_page.get_template(request), {
                'page': error_page,
                'request': request,
            }, status=404)
    except Custom404Page.DoesNotExist:
        pass

    return render(request, "404.html", status=404)  # fallback

handler404 = 'core.urls.wagtail_custom_404'
