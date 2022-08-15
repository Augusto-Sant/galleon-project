from django import forms
from django.forms import ModelForm
from django.core import validators

#ALL QUIZZES HERE

class pt_quiz(forms.Form):
    """Portugal Quiz Form"""
    #in choices (value,label), label = title of question
    CHOICES_1 = [("A1","Discovered a sea route to India"),("A2","Discovered Brazil"),("A3","Great commander in the Reconquista"),]
    answer_1 = forms.ChoiceField(choices=CHOICES_1, widget=forms.RadioSelect,label="1. What is Vasco da Gama known for?")

    CHOICES_2 = [("A1","Juan Ruiz"),("A2","Luís de Camões"),("A3","Miguel de Cervantes"),]
    answer_2 = forms.ChoiceField(choices=CHOICES_2, widget=forms.RadioSelect,label="2. Who is considered the greatest portuguese poet?")

    CHOICES_3 = [("A1","A Roman city"),("A2","A Dinasty name"),("A3","A famous andalusian conqueror"),]
    answer_3 = forms.ChoiceField(choices=CHOICES_3, widget=forms.RadioSelect,label="3. What originated the name Portugal?")

class an_quiz(forms.Form):
    """Andalusia Quiz Form"""
    #in choices (value,label), label = title of question
    CHOICES_1 = [("A1","Islam"),("A2","Christianity"),("A3","Judaism"),]
    answer_1 = forms.ChoiceField(choices=CHOICES_1, widget=forms.RadioSelect,label="1. What was the religion of the rulers in Al-Andalus?/Andalusia")

    CHOICES_2 = [("A1","Abbasid"),("A2","Rashidun"),("A3","Umayyad"),]
    answer_2 = forms.ChoiceField(choices=CHOICES_2, widget=forms.RadioSelect,label="2. Most known dinasty/clan in Andalusia")

    CHOICES_3 = [("A1","Aragon"),("A2","Cordoba"),("A3","Granada"),]
    answer_3 = forms.ChoiceField(choices=CHOICES_3, widget=forms.RadioSelect,label="3. Last muslim emirate in hispania?")

class nu_quiz(forms.Form):
    """Nubia Quiz Form"""
    #in choices (value,label), label = title of question
    CHOICES_1 = [("A1","Ghana"),("A2","Morroco"),("A3","Egypt"),]
    answer_1 = forms.ChoiceField(choices=CHOICES_1, widget=forms.RadioSelect,label="1. Which country Nubia was connected with and sometimes ruled?")

    CHOICES_2 = [("A1","Tunisia"),("A2","Kush"),("A3","Ethiopia"),]
    answer_2 = forms.ChoiceField(choices=CHOICES_2, widget=forms.RadioSelect,label="2. What is the other name Nubia is known?")

    CHOICES_3 = [("A1","Akhenaten"),("A2","Tutankamon"),("A3","Piye"),]
    answer_3 = forms.ChoiceField(choices=CHOICES_3, widget=forms.RadioSelect,label="3. Most famous nubian Pharaoh?")

class en_quiz(forms.Form):
    """England Quiz Form"""
    #in choices (value,label), label = title of question
    CHOICES_1 = [("A1","Anglo-Saxon/Norman/Britons"),("A2","Swedish/German/Britons"),("A3","Romans/Polish/Britons"),]
    answer_1 = forms.ChoiceField(choices=CHOICES_1, widget=forms.RadioSelect,label="1. What were the main cultures that made the English?")

    CHOICES_2 = [("A1","William"),("A2","Henry IV"),("A3","Athelstan"),]
    answer_2 = forms.ChoiceField(choices=CHOICES_2, widget=forms.RadioSelect,label="2. Who defeated the vikings and unified England?")

    CHOICES_3 = [("A1","Harold Godwinson"),("A2","William of Normandy"),("A3","Harald Hardrada"),]
    answer_3 = forms.ChoiceField(choices=CHOICES_3, widget=forms.RadioSelect,label="3. Who won the famous Battle of Hastings?")

class br_quiz(forms.Form):
    """Brazil Quiz Form"""
    #in choices (value,label), label = title of question
    CHOICES_1 = [("A1","Gold/Sky/Rivers/Forests"),("A2","Amazon/Ocean/Portugal"),("A3","Peace/Faith/Honor"),]
    answer_1 = forms.ChoiceField(choices=CHOICES_1, widget=forms.RadioSelect,label="1. What the colors of brazil flag stand for now?")

    CHOICES_2 = [("A1","Braganza Dinasty/Habsburg Dinasty"),("A2","Amazon/Portugal"),("A3","Chistianity/Prosperity"),]
    answer_2 = forms.ChoiceField(choices=CHOICES_2, widget=forms.RadioSelect,label="2. What the colors of brazil flag stood for?")

    CHOICES_3 = [("A1","By the son and heir of a portuguese king"),("A2","By an armed revolution by the people"),("A3","Napoleon Invasion"),]
    answer_3 = forms.ChoiceField(choices=CHOICES_3, widget=forms.RadioSelect,label="3. How brazil became independent?")