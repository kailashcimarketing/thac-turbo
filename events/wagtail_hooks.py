from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import Category, Events

class EvntsCategoryViewSet(SnippetViewSet):
    model = Category
    menu_label = "Categories"
    list_display  = ("title",'weight',)
    
    search_fields = ("title",)

class EventsViewSet(SnippetViewSet):
    model = Events
    menu_label = "Events"
    list_display  = ("title",'start_date','end_date','release_date','status','weight')
    search_fields = ("title",)


class EventsGroup(SnippetViewSetGroup):
    menu_label = "Events"
    menu_icon = "bars"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        EvntsCategoryViewSet,
        EventsViewSet,
        
    )

register_snippet(EventsGroup)
