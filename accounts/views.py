from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View,TemplateView
#accounts APPS ARE ALL THINGS RELATED TO ACCOUNT/LOGIN/SIGN UP
from . import models

#HOME PRINCIPAL --
class IndexView(TemplateView):
    """Main index of galleon."""
    template_name = 'accounts/index.html'

#About page
class AboutView(TemplateView):
    """About template view in accounts"""
    template_name = 'accounts/about.html'

#PROFILE --
def all_profiles_view(request):
    """Return all profiles registered in site ordered by points"""
    profiles_list = models.UserProfile.objects.order_by('-profile_points')[:10]
    return render(request,'accounts/profile_scoreboard.html',{"all_users":profiles_list})

def profile_view(request,user_profile_id):
    """returns profile.html with a profile context"""
    profiles_list = models.UserProfile.objects.order_by('id')
    profile = profiles_list[user_profile_id-1]
    return render(request,'accounts/profile.html',{"profile":profile})

#LOGIN SYSTEM --
def login_form_view(request):
    """returns view of login form"""
    registered = False
    
    form = forms.User_form()
    if request.method == 'POST':
        form = forms.User_form(request.POST)#TAKE WHAT WAS PUT 

        if form.is_valid():
            # DO SOMETHING CODE
            user = form.save()#SAVE NEW USER CREATED
            user.set_password(user.password)#CREATES PASSWORD HASH
            user.save()#SAVES USER
            registered = True#MARKS AS REGISTERED
    else:
        # Was not an HTTP post so we just render the forms as blank.
        form = forms.User_form()

    return render(request,"accounts/sign_in.html",{'form':form,'registered':registered,})

def user_login(request):
    """User login, gets username and password and authenticates."""
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, "accounts/login.html", {})

@login_required #REQUIRES LOGIN TO SEE
def user_logout(request):
    """User logout."""
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

