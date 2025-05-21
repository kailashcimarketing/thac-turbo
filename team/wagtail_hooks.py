from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import Team, Category, Coaches, Tutors,Instructors, Boardmember

class TeamViewSet(SnippetViewSet):
    model = Team
    menu_label = "Leadership Team"
    ordering = ("title",)
    list_display  =["title","position","status","weight",]
    search_fields = ("title",)
    icon = "user"
    #add_to_admin_menu = True

class CoachesViewSet(SnippetViewSet):
    model = Coaches
    menu_label = "Coaches"
    ordering = ("title",)
    list_display  =["title","position","status","weight",]
    search_fields = ("title",)  
    icon = "user"  

class TutorsViewSet(SnippetViewSet):
    model = Tutors
    menu_label = "Tutors"
    ordering = ("title",)
    list_display  =["title","position","status","weight",]
    search_fields = ("title",)   
    icon = "user" 

class InstructorsViewSet(SnippetViewSet):
    model = Instructors
    menu_label = "Instructors"
    ordering = ("title",)
    list_display  =["title","position","status","weight",]
    search_fields = ("title",)   
    icon = "user" 

class BoardmemberViewSet(SnippetViewSet):
    model = Boardmember
    menu_label = "Board Members"
    ordering = ("title",)
    list_display  =["title","position","status","weight",]
    search_fields = ("title",)   
    icon = "user"     

class CatgoryViewSet(SnippetViewSet):
    model = Category
    menu_label = "Leadership Categories"
    ordering = ("title",)
    search_fields = ("title",)
    #add_to_admin_menu = True
    icon = "list-ol"
    menu_order = 201  # will put in 3rd place (000 being 1st, 100 2nd)





class TeamGroup(SnippetViewSetGroup):
    menu_label = "Profiles"
    menu_icon = "bars"  # change as required
    menu_order = 202  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        CatgoryViewSet,
        TeamViewSet,
        BoardmemberViewSet,
        TutorsViewSet,
        CoachesViewSet,        
        InstructorsViewSet        
    )

register_snippet(TeamGroup)
