from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import Category, News

class NewsCategoryViewSet(SnippetViewSet):
    model = Category
    menu_label = "Categories"
    list_display  = ("title",'weight',)
    
    search_fields = ("title",)

class NewsViewSet(SnippetViewSet):
    model = News
    menu_label = "News"
    list_display  = ("title",'release_date','status',)
    search_fields = ("title",)


class NewsGroup(SnippetViewSetGroup):
    menu_label = "News"
    menu_icon = "bars"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        NewsCategoryViewSet,
        NewsViewSet,
        
    )

register_snippet(NewsGroup)
