from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import ContentHolder, DynamicContentSnippet, PhotoGallery, PortalMenu


class PortalMenuViewSet(SnippetViewSet):
    model = PortalMenu
    menu_label = "Portal Menu"
    ordering = ("title",'image','url','weight',)
    list_display = ordering = ("title",'url','weight',)
    search_fields = ("title",)
    add_to_admin_menu = False
    add_to_settings_menu = True

register_snippet(PortalMenuViewSet)    

class PhotoGalleryViewSet(SnippetViewSet):
    model = PhotoGallery
    menu_label = "Photo Galleries"
    ordering = ("title",)
    search_fields = ("title",)
    add_to_admin_menu = True

register_snippet(PhotoGalleryViewSet)    

class CHSnippetViewSet(SnippetViewSet):
    model = ContentHolder
    menu_label = "Content Holders"
    ordering = ("title",)
    search_fields = ("title",)

class DynamicCHSnippetViewSet(SnippetViewSet):
    model = DynamicContentSnippet
    menu_label = "Dynamic Content Snippet"
    ordering = ("title",)
    search_fields = ("title",)


class CHSnippetGroup(SnippetViewSetGroup):
    menu_label = "Content Holders"
    menu_icon = "bars"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        CHSnippetViewSet,
        DynamicCHSnippetViewSet,
        
    )

register_snippet(CHSnippetGroup)
