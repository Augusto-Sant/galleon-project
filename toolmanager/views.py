from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from django.http import HttpResponseRedirect, HttpResponse
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
    #         answer_2 = form.cleaned_data['answer_2']
    #         answer_3 = form.cleaned_data['answer_3']
    #         user = UserProfile.objects.get(user_id=request.user.id)
            
    #         #check answers
    #         points_gained = 0
    #         if answer_1 == "A1":
    #             points_gained += 5
            
    #         if answer_2 == "A2":
    #             points_gained += 5
            
    #         if answer_3 == "A1":
    #             points_gained += 5
            
    #         user.add_points(points_gained)
    #         return render(request,"toolmanager/answer_portugal.html",{'points_gained':points_gained})
def quiz_view(request,quiz_num):
    """returns quiz form html or answer html"""
    if quiz_num == 0:
        #portugal
        country_name = "Portugal"
        back = "pt_back"
        form = forms.pt_quiz(request.POST)
    elif quiz_num == 1:
        #andalusia
        country_name = "Andalusia"
        back = "an_back"
        form = forms.an_quiz(request.POST)
    elif quiz_num == 2:
        #nubia
        country_name = "Nubia"
        back = "nu_back"
        form = forms.nu_quiz(request.POST)
    elif quiz_num == 3:
        #england
        country_name = "England"
        back = "en_back"
        form = forms.en_quiz(request.POST)
    elif quiz_num == 4:
        #brazil
        country_name = "Brazil"
        back = "br_back"
        form = forms.br_quiz(request.POST)
    
    if request.method == "POST":
        if form.is_valid():
            answer_1 = form.cleaned_data['answer_1']
            answer_2 = form.cleaned_data['answer_2']
            answer_3 = form.cleaned_data['answer_3']
            user = UserProfile.objects.get(user_id=request.user.id)
            
            #check answers
            points_gained = 0
            if quiz_num == 0:
                answers = ["A1","A2","A1"]
            elif quiz_num == 1:
                answers = ["A1","A3","A3"]
            elif quiz_num == 2:
                answers = ["A3","A2","A3"]
            elif quiz_num == 3:
                answers = ["A1","A3","A2"]
            elif quiz_num == 4:
                answers = ["A1","A1","A1"]

            if answer_1 == answers[0]:
                points_gained += 5
            
            if answer_2 == answers[1]:
                points_gained += 5
            
            if answer_3 == answers[2]:
                points_gained += 5
            
            user.add_points(points_gained)
            return render(request,"toolmanager/answer_quiz.html",{"Q1":answers[0],"Q2":answers[1],"Q3":answers[2]})
    
    return render(request,"toolmanager/quiz_form.html",{"country_name":country_name,"back":back,"form":form})