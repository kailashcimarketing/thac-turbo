from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import Team, Category, Coaches, Tutors,Instructors

class TeamViewSet(SnippetViewSet):
    model = Team
    menu_label = "Team"
    ordering = ("title",)
    list_display  =["title","position","status","weight",]
    search_fields = ("title",)
    #add_to_admin_menu = True

class CoachesViewSet(SnippetViewSet):
    model = Coaches
    menu_label = "Coaches"
    ordering = ("title",)
    list_display  =["title","position","status","weight",]
    search_fields = ("title",)    

class TutorsViewSet(SnippetViewSet):
    model = Tutors
    menu_label = "Tutors"
    ordering = ("title",)
    list_display  =["title","position","status","weight",]
    search_fields = ("title",)    

class InstructorsViewSet(SnippetViewSet):
    model = Instructors
    menu_label = "Instructors"
    ordering = ("title",)
    list_display  =["title","position","status","weight",]
    search_fields = ("title",)    

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
        CoachesViewSet,
        TutorsViewSet,
        InstructorsViewSet        
    )

register_snippet(TeamGroup)
