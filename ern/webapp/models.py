"""Webapp models file."""
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

SEX_ENUM = {
    "M": "Male",
    "F": "Female",
    "O": "Other/Unspecified/Prefer not to say"
}

LANG_ENUM = {
    "nl": "Nederlands",
    "en": "English",
}

class Sample(models.Model):
    """Primary model for participant data."""


    timestamp = models.DateTimeField(auto_now_add=True)


    language = models.CharField(choices=SEX_ENUM, default="nl", max_length=2)
    sex = models.CharField(choices=SEX_ENUM, default="O", max_length=1)
    age = models.IntegerField(default=18, validators=[MinValueValidator(12), MaxValueValidator(99)])

    story_text = models.CharField(max_length=500)
    human_shuffled_story = models.CharField(max_length=500)
    random_shuffled_story = models.CharField(max_length=500)
    llm_reconstructed_story = models.CharField(max_length=500)
    rating_reconstructed_fluency = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
    rating_reconstructed_flow = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
    rating_reconstructed_accuracy = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])