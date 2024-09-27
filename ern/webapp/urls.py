"""Webapp urls file."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("why", views.why, name="why"),
    path("what", views.what, name="what"),
    path("how", views.how, name="how"),
    path("other", views.other, name="other"),
    path("consent", views.consent, name="consent"),
    path("demographics", views.demographics, name="demographics"),
    path("enter_story", views.enter_story, name="enter_story"),
    path("shuffle_story", views.shuffle_story, name="shuffle_story"),
    path("next_reconstruction", views.next_reconstruction, name="next_reconstruction"),
    path(
        "rate_human_shuffle_reconstructed",
        views.rate_human_shuffle_reconstructed,
        name="rate_human_shuffle_reconstructed",
    ),
    path(
        "rate_random_shuffle_reconstructed",
        views.rate_random_shuffle_reconstructed,
        name="rate_random_shuffle_reconstructed",
    ),
    path("thank_you", views.thank_you, name="thank_you"),
]
