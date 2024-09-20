"""Webapp models file."""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

SEX_ENUM = [
    ("P", "Prefer not to say"),
    ("O", "Other/Unspecified"),
    ("M", "Male"),
    ("F", "Female"),
]

LANG_ENUM = [
    ("nl", "Nederlands"),
    ("en", "English"),
]


class Sample(models.Model):  # noqa: DJ008
    """Primary model for participant data."""

    timestamp = models.DateTimeField(auto_now_add=True)

    language = models.CharField(choices=LANG_ENUM, default="nl", max_length=2)
    sex = models.CharField(choices=SEX_ENUM, default="P", max_length=1)
    age = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])

    story_text = models.CharField(max_length=2000)
    human_shuffled_story = models.CharField(max_length=2500)
    human_shuffled_story_difficulty = models.IntegerField(
        default=5, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    random_shuffled_story = models.CharField(max_length=2500)

    llm_reconstructed_human_story = models.CharField(default="", max_length=2500)
    rating_reconstructed_human_fluency = models.IntegerField(
        default=5, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    rating_reconstructed_human_flow = models.IntegerField(
        default=5, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    rating_reconstructed_human_accuracy = models.IntegerField(
        default=5, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    llm_reconstructed_random_story = models.CharField(default="", max_length=2500)
    rating_reconstructed_random_fluency = models.IntegerField(
        default=5, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    rating_reconstructed_random_flow = models.IntegerField(
        default=5, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    rating_reconstructed_random_accuracy = models.IntegerField(
        default=5, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
