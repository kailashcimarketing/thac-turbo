from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import Team, Category

class TeamViewSet(SnippetViewSet):
    model = Team
    menu_label = "Team"
    ordering = ("title",)
    list_display  =["title","position","status","weight",]
    list_filter = ["catgory"]
    search_fields = ("title",)
    #add_to_admin_menu = True

class CatgoryViewSet(SnippetViewSet):
    model = Category
    menu_label = "Categories"
    ordering = ("title",)
    search_fields = ("title",)



class TeamGroup(SnippetViewSetGroup):
    menu_label = "Team"
    menu_icon = "bars"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        CatgoryViewSet,
        TeamViewSet,
        
    )

register_snippet(TeamGroup)
