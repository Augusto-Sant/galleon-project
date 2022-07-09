from django.urls import path
from toolmanager import views


app_name = "toolmanager"

urlpatterns = [
    path("",views.tools_index,name="tool_index"),
    path("buy",views.tool_buy,name="tool_buy"),
    #Quiz/voyages--
    path("portugal",views.portugal_quiz_view,name="portugal_view"),
    path("andalusia",views.andalusia_quiz_view,name="andalusia_view"),
    path("nubia",views.nubia_quiz_view,name="nubia_view"),
    path("england",views.england_quiz_view,name="england_view"),
    path("brazil",views.brazil_quiz_view,name="brazil_view"),
]