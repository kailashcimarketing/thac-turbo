from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import Vacancies, Category

class VacanciesViewSet(SnippetViewSet):
    model = Vacancies
    menu_label = "Vacancies"
    ordering = ("title",)
    list_display  =["title","catgory","start_date","end_date","status_icon","weight"]
    search_fields = ("title",)
    #add_to_admin_menu = True

class CatgoryViewSet(SnippetViewSet):
    model = Category
    menu_label = "Categories"
    ordering = ("title",)
    search_fields = ("title",)



class VacanciesGroup(SnippetViewSetGroup):
    menu_label = "Vacancies"
    menu_icon = "bars"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        CatgoryViewSet,
        VacanciesViewSet,
        
    )

register_snippet(VacanciesGroup)
