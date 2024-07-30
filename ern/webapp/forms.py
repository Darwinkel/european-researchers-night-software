"""Django form definitions."""

from django import forms

from .models import SEX_ENUM

from .widgets import BootstrapCheckboxInput, BootstrapSelectInput, BootstrapIntegerInput, BootstrapTextAreaInput


class ConsentForm(forms.Form):
    template_name = "bootstrap_form_checkbox.html"
    q1 = forms.BooleanField(
        widget=BootstrapCheckboxInput(),
        required=True,
        label="I have read and understood the information about the research project and I voluntarily agree to participate.",
    )
    q2 = forms.BooleanField(
        widget=BootstrapCheckboxInput(),
        required=True, label="I understand that I can withdraw at any time, without giving a reason."
    )
    q3 = forms.BooleanField(
        widget=BootstrapCheckboxInput(),
        required=True, label="I understand that taking part in the study involves interacting with an AI agent."
    )
    q4 = forms.BooleanField(
        widget=BootstrapCheckboxInput(),
        required=True,
        label="That the data collected through the games that I provide will be deposited in DataverseNL so that it can be used for future research and learning.",
    )
    q5 = forms.BooleanField(
        widget=BootstrapCheckboxInput(),
        required=True,
        label="I know whom to contact in case I have questions and I have been informed about my rights.",
    )


class DemographicsForm(forms.Form):
    template_name = "bootstrap_form.html"
    sex = forms.ChoiceField(choices=SEX_ENUM, required=False, label="Sex",        widget=BootstrapSelectInput(),)
    age = forms.IntegerField(
        initial=0, min_value=0, max_value=99, required=False, label="Age (set to '0' if you prefer not to say)", widget=BootstrapIntegerInput()
    )


class StoryForm(forms.Form):
    template_name = "bootstrap_form.html"
    story_text = forms.CharField(required=True, label="Story", widget=BootstrapTextAreaInput())

class ReshuffleForm(forms.Form):
    template_name = "bootstrap_form.html"
    difficulty = forms.IntegerField(initial=5, min_value=0, max_value=10, required=True, label="Reconstruction difficulty", widget=BootstrapIntegerInput())

class RateReconstructionForm(forms.Form):
    template_name = "bootstrap_form.html"
    flow = forms.IntegerField(initial=5, min_value=0, max_value=10, required=True, label="Flow", widget=BootstrapIntegerInput())
    fluency = forms.IntegerField(initial=5, min_value=0, max_value=10, required=True, label="Fluency", widget=BootstrapIntegerInput())
    accuracy = forms.IntegerField(initial=5, min_value=0, max_value=10, required=True, label="Accuracy", widget=BootstrapIntegerInput())
