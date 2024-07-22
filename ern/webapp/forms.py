

from django import forms
from .models import SEX_ENUM


class ConsentForm(forms.Form):
    q1 = forms.BooleanField(required=True, label="I have read and understood the information about the research project and I voluntarily agree to participate. I know whom to contact in case I have questions and I have been informed about my rights.")
    q2 = forms.BooleanField(required=True, label="I understand that I can withdraw at any time, without giving a reason.")
    q3 = forms.BooleanField(required=True, label="I understand that taking part in the study involves interacting with an AI agent.")
    q4 = forms.BooleanField(required=True, label="That the data collected through the games that I provide will be deposited in DataverseNL so that it can be used for future research and learning.")

class DemographicsForm(forms.Form):

    sex = forms.ChoiceField(choices=SEX_ENUM, required=False, label='Sex')
    age = forms.IntegerField(initial='', required=False, label='Age')

class StoryForm(forms.Form):
    story_text = forms.CharField(required=True, label='Story', widget=forms.Textarea)

class ShuffleStoryForm(forms.Form):
    human_shuffled_story = forms.CharField(required=True, label='Shuffled story', widget=forms.Textarea)

class RateReconstructionForm(forms.Form):
    fluency = forms.IntegerField(min_value=0, required=False, label='Fluency')
    flow = forms.IntegerField(min_value=0, required=False, label='Flow')
    accuracy = forms.IntegerField(min_value=0, required=False, label='Accuracy')

