from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View,TemplateView
#APP GAL APPS ARE ALL THINGS RELATED TO ACCOUNT/LOGIN/SIGN UP

#HOME PRINCIPAL --
class IndexView(TemplateView):
    template_name = 'AppGal/index.html'

#About page
class AboutView(TemplateView):
    template_name = 'AppGal/about.html'

#PROFILE --
class ProfileView(TemplateView):
    template_name = 'AppGal/profile.html'

#LOGIN SYSTEM --
def login_form_view(request):
    
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

    return render(request,"AppGal/sign_in.html",{'form':form,'registered':registered,})

def user_login(request):

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
        return render(request, "AppGal/login.html", {})

@login_required #REQUIRES LOGIN TO SEE
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

