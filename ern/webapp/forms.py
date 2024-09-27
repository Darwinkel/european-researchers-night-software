"""Django form definitions."""

from django import forms

from .models import SEX_ENUM
from .widgets import BootstrapCheckboxInput, BootstrapIntegerInput, BootstrapSelectInput, BootstrapTextAreaInput


class ConsentForm(forms.Form):
    """Consent form."""

    template_name = "bootstrap_form_checkbox.html"
    q1 = forms.BooleanField(
        widget=BootstrapCheckboxInput(),
        required=True,
        label="I have read and understood the information about the research project "
        "and I voluntarily agree to participate.",
    )
    q2 = forms.BooleanField(
        widget=BootstrapCheckboxInput(),
        required=True,
        label="I understand that I can withdraw at any time, without giving a reason.",
    )
    q3 = forms.BooleanField(
        widget=BootstrapCheckboxInput(),
        required=True,
        label="I understand that taking part in the study involves interacting with an AI agent.",
    )
    q4 = forms.BooleanField(
        widget=BootstrapCheckboxInput(),
        required=True,
        label="I understand that the data collected through the stories that I provide will be deposited in DataverseNL "
        "so that it can be used for future research and learning.",
    )
    q5 = forms.BooleanField(
        widget=BootstrapCheckboxInput(),
        required=True,
        label="I know whom to contact in case I have questions and I have been informed about my rights.",
    )


class DemographicsForm(forms.Form):
    """Demographics form."""

    template_name = "bootstrap_form.html"
    sex = forms.ChoiceField(
        choices=SEX_ENUM,
        required=False,
        label="Gender",
        widget=BootstrapSelectInput(),
    )
    age = forms.IntegerField(
        initial=0,
        min_value=0,
        max_value=99,
        required=False,
        label="Age (set to '0' if you prefer not to say)",
        widget=BootstrapIntegerInput(),
    )


class StoryForm(forms.Form):
    """Story form."""

    template_name = "bootstrap_form.html"
    story_text = forms.CharField(required=True, label="Story", widget=BootstrapTextAreaInput())


class ReshuffleForm(forms.Form):
    """Reshuffle form."""

    template_name = "bootstrap_form.html"
    difficulty = forms.IntegerField(
        initial=5,
        min_value=0,
        max_value=10,
        required=True,
        label="Reconstruction difficulty",
        widget=BootstrapIntegerInput(),
    )


class RateReconstructionForm(forms.Form):
    """Rate reconstruction form (both human and random)."""

    template_name = "bootstrap_form.html"
    quality = forms.IntegerField(
        initial=5,
        min_value=0,
        max_value=10,
        required=True,
        label="How good is this reconstruction?",
        widget=BootstrapIntegerInput(),
    )
    niceness = forms.IntegerField(
        initial=5,
        min_value=0,
        max_value=10,
        required=True,
        label="The story might be different from the original. Do you like this particular story now?",
        widget=BootstrapIntegerInput(),
    )
