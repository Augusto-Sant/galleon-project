from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
#TOOLMANAGER VIEWS/VOYAGES  --
from django.contrib.auth import get_user_model
User = get_user_model()
#forms
from toolmanager import forms


#INDEX PRINCIPAL --
#Tools--
def tools_index(request):
    """Returns index html of toolmanager"""
    tool_list = models.Tool.objects.order_by("price")
    context = {'tool_list': tool_list}

    return render(request, 'toolmanager/index.html', context)

@login_required
def tool_buy(request):
    """Buy and subtract points from user."""
    if request.method == "POST":
        user = UserProfile.objects.get(user_id=request.user.id)
        
        if "portugal_form" in request.POST:
            price = 5
            user.portugal = True
            if user.profile_points > 0:
                user.sub_points(price)
        elif "andalusia_form" in request.POST:
            price = 10
            user.andalusia = True
            if user.profile_points > 0:
                user.sub_points(price)
        elif "nubia_form" in request.POST:
            price = 15
            user.nubia = True
            if user.profile_points > 0:
                user.sub_points(price)
        elif "england_form" in request.POST:
            price = 20
            user.england = True
            if user.profile_points > 0:
                user.sub_points(price)
        elif "brazil_form" in request.POST:
            price = 25
            user.brazil = True
            if user.profile_points > 0:
                user.sub_points(price)
    
    return render(request, "toolmanager/index.html", {})

#Voyages/Quiz ---
def portugal_quiz_view(request):
    """returns Portugal quiz html"""
    if request.method == "POST":
        form = forms.pt_quiz(request.POST)
        if form.is_valid():
            answer_1 = form.cleaned_data['answer_1']
            answer_2 = form.cleaned_data['answer_2']
            answer_3 = form.cleaned_data['answer_3']
            user = UserProfile.objects.get(user_id=request.user.id)
            
            #check answers
            points_gained = 0
            if answer_1 == "A1":
                points_gained += 5
            
            if answer_2 == "A2":
                points_gained += 5
            
            if answer_3 == "A1":
                points_gained += 5
            
            user.add_points(points_gained)
            return render(request,"toolmanager/answer_portugal.html",{'points_gained':points_gained})
    else:
        form = forms.pt_quiz()
    
    return render(request,"toolmanager/portugal.html",{'form':form})

def andalusia_quiz_view(request):
    """returns Andalusia quiz html"""
    if request.method == "POST":
        form = forms.an_quiz(request.POST)
        if form.is_valid():
            answer_1 = form.cleaned_data['answer_1']
            answer_2 = form.cleaned_data['answer_2']
            answer_3 = form.cleaned_data['answer_3']
            user = UserProfile.objects.get(user_id=request.user.id)
            
            #check answers
            points_gained = 0
            if answer_1 == "A1":
                points_gained += 10
            
            if answer_2 == "A3":
                points_gained += 10
            
            if answer_3 == "A3":
                points_gained += 10
            
            user.add_points(points_gained)
            return render(request,"toolmanager/answer_andalusia.html",{'points_gained':points_gained})
    else:
        form = forms.an_quiz()
    
    return render(request,"toolmanager/andalusia.html",{'form':form})

def nubia_quiz_view(request):
    """returns Nubia quiz html"""
    if request.method == "POST":
        form = forms.nu_quiz(request.POST)
        if form.is_valid():
            answer_1 = form.cleaned_data['answer_1']
            answer_2 = form.cleaned_data['answer_2']
            answer_3 = form.cleaned_data['answer_3']
            user = UserProfile.objects.get(user_id=request.user.id)
            
            #check answers
            points_gained = 0
            if answer_1 == "A3":
                points_gained += 10
            
            if answer_2 == "A2":
                points_gained += 10
            
            if answer_3 == "A3":
                points_gained += 10
            
            user.add_points(points_gained)
            return render(request,"toolmanager/answer_nubia.html",{'points_gained':points_gained})
    else:
        form = forms.nu_quiz()
    
    return render(request,"toolmanager/nubia.html",{'form':form})

def england_quiz_view(request):
    """returns England quiz html"""
    if request.method == "POST":
        form = forms.en_quiz(request.POST)
        if form.is_valid():
            answer_1 = form.cleaned_data['answer_1']
            answer_2 = form.cleaned_data['answer_2']
            answer_3 = form.cleaned_data['answer_3']
            user = UserProfile.objects.get(user_id=request.user.id)
            
            #check answers
            points_gained = 0
            if answer_1 == "A1":
                points_gained += 10
            
            if answer_2 == "A3":
                points_gained += 10
            
            if answer_3 == "A2":
                points_gained += 10
            
            user.add_points(points_gained)
            return render(request,"toolmanager/answer_england.html",{'points_gained':points_gained})
    else:
        form = forms.en_quiz()
    
    return render(request,"toolmanager/england.html",{'form':form})

def brazil_quiz_view(request):
    """returns Brazil quiz html"""
    if request.method == "POST":
        form = forms.br_quiz(request.POST)
        if form.is_valid():
            answer_1 = form.cleaned_data['answer_1']
            answer_2 = form.cleaned_data['answer_2']
            answer_3 = form.cleaned_data['answer_3']
            user = UserProfile.objects.get(user_id=request.user.id)
            
            #check answers
            points_gained = 0
            if answer_1 == "A1":
                points_gained += 15
            
            if answer_2 == "A1":
                points_gained += 15
            
            if answer_3 == "A1":
                points_gained += 15
            
            user.add_points(points_gained)
            return render(request,"toolmanager/answer_brazil.html",{'points_gained':points_gained})
    else:
        form = forms.br_quiz()
    
    return render(request,"toolmanager/brazil.html",{'form':form})