from django.urls import path
from marketplace import views

app_name = "marketplace"#name of app to be able to link
#{% url 'marketplace:index' %} using this to link

urlpatterns = [
    path("",views.marketindex,name="marketindex"),
    path("buy",views.market_buy,name="marketbuy"),
]