

from django import forms
from .models import SEX_ENUM


class ConsentForm(forms.Form):
    q1 = forms.BooleanField(required=True, label="I have read and understood the information about the research project and I voluntarily agree to participate. I know whom to contact in case I have questions and I have been informed about my rights.")
    q2 = forms.BooleanField(required=True, label="I understand that I can withdraw at any time, without giving a reason.")
    q3 = forms.BooleanField(required=True, label="I understand that taking part in the study involves interacting with an AI agent.")
    q4 = forms.BooleanField(required=True, label="That the data collected through the games that I provide will be deposited in DataverseNL so that it can be used for future research and learning.")

class DemographicsForm(forms.Form):

    sex = forms.ChoiceField(choices=SEX_ENUM, required=False, label='Sex')
    age = forms.IntegerField(initial='', min_value=0, max_value=99, required=False, label='Age (leave blank if you prefer not to say)')

class StoryForm(forms.Form):
    story_text = forms.CharField(required=True, label='Story', widget=forms.Textarea)

class RateReconstructionForm(forms.Form):
    flow = forms.IntegerField(min_value=0, max_value=10, required=True, label='Flow')
    fluency = forms.IntegerField(min_value=0, max_value=10, required=True, label='Fluency')
    accuracy = forms.IntegerField(min_value=0, max_value=10, required=True, label='Accuracy')

