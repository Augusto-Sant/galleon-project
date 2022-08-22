from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.views.generic import View,TemplateView

# Create your views here.
def marketindex(request):
    return render(request,'marketplace/index.html',{})

@login_required
def market_buy(request):
    """Buy and subtract points from user."""
    if request.method == "POST":
        user = UserProfile.objects.get(user_id=request.user.id)
        
        if "buy_collection1" in request.POST:
            price = 10
            user.img_collection_1 = True
            if user.profile_points > 0:
                user.sub_points(price)
    
    return render(request, 'marketplace/index.html', {})