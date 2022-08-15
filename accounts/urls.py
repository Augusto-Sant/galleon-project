from django.urls import path
from accounts import views

#accounts APPS ARE ALL THINGS RELATED TO ACCOUNT/LOGIN/SIGN UP
app_name = "accounts"#name of app to be able to link
#{% url 'accounts:index' %} using this to link

urlpatterns = [
    path("login/",views.login_form_view,name="login_form_view"),
    path("user_login",views.user_login,name='user_login'),
    path('logout/',views.user_logout,name="logout"),#main logout link
    path("profile/",views.ProfileView.as_view(),name="profile_view"),
    path("about/",views.AboutView.as_view(),name="about_view")
]