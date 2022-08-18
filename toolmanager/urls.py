from django.urls import path
from toolmanager import views


app_name = "toolmanager"

urlpatterns = [
    path("",views.tools_index,name="tool_index"),
    path("buy",views.tool_buy,name="tool_buy"),
    #Quiz/voyages--
    path("quiz/<int:quiz_num>",views.quiz_view,name="quiz_view")
]