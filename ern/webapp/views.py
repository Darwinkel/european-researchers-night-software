"""Webapp views."""

import random
from datetime import UTC, datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from nltk.tokenize import sent_tokenize

from .forms import ConsentForm, DemographicsForm, RateReconstructionForm, ReshuffleForm, StoryForm
from .llms import reconstruct_with_llm
from .models import Sample


def index(request: HttpRequest) -> HttpResponse:
    """Index/default switch language view."""
    if "sample_id" in request.session:
        del request.session["sample_id"]
    return render(request, "00_language.html")


def why(request: HttpRequest) -> HttpResponse:
    """Why view."""
    return render(request, "01a_why.html")


def what(request: HttpRequest) -> HttpResponse:
    """Info view."""
    return render(request, "01b_what.html")


def how(request: HttpRequest) -> HttpResponse:
    """How view."""
    return render(request, "01c_how.html")


def other(request: HttpRequest) -> HttpResponse:
    """Other view."""
    return render(request, "01d_other.html")


def next_reconstruction(request: HttpRequest) -> HttpResponse:
    """Next reconstruction view."""
    return render(request, "04a_next_reconstruction.html")


def consent(request: HttpRequest) -> HttpResponse:
    """Consent view."""
    if request.method == "POST":
        form = ConsentForm(request.POST)

        if form.is_valid():
            return redirect("demographics")

    else:
        form = ConsentForm()
    return render(
        request,
        "01e_consent.html",
        {
            "form": form,
        },
    )


def demographics(request: HttpRequest) -> HttpResponse:
    """Demographics view."""
    if request.method == "POST":
        form = DemographicsForm(request.POST)

        if form.is_valid():
            sample = Sample(
                timestamp=datetime.now(tz=UTC),
                language=request.LANGUAGE_CODE,
                sex=form.cleaned_data["sex"],
                age=form.cleaned_data["age"],
            )
            sample.save()
            request.session["sample_id"] = sample.id
            return redirect("enter_story")

    else:
        form = DemographicsForm()
    return render(
        request,
        "02a_enter_demographics.html",
        {
            "form": form,
        },
    )


def enter_story(request: HttpRequest) -> HttpResponse:
    """Enter story view."""
    sample = Sample.objects.get(pk=request.session["sample_id"])
    if request.method == "POST":
        form = StoryForm(request.POST)

        if form.is_valid():
            sample.story_text = form.cleaned_data["story_text"]
            sample.save()
            return redirect("shuffle_story")

    else:
        form = StoryForm()
    return render(
        request,
        "02_enter_story.html",
        {
            "form": form,
            "sample_id": sample.id,
        },
    )


def shuffle_story(request: HttpRequest) -> HttpResponse:
    """Shuffle story view."""
    sample = Sample.objects.get(pk=request.session["sample_id"])

    if request.method == "POST":
        print(request.POST)
        sample.human_shuffled_story = str(request.POST.getlist("dragdrop_list"))
        sample.human_shuffled_story_difficulty = int(request.POST.get("difficulty"))  # type: ignore[arg-type]

        tokenized_story = sent_tokenize(sample.story_text)
        sample.random_shuffled_story = random.sample(tokenized_story, len(tokenized_story))  # type: ignore[assignment]

        sample.llm_reconstructed_human_story, sample.llm_reconstructed_random_story = reconstruct_with_llm(
            request.LANGUAGE_CODE, sample.human_shuffled_story, sample.random_shuffled_story
        )

        sample.save()
        return redirect("rate_human_shuffle_reconstructed")

    form = ReshuffleForm()

    return render(
        request,
        "03_shuffle_story.html",
        {
            "form": form,
            "sample_id": sample.id,
            "tokenized_story_text": sent_tokenize(sample.story_text),
        },
    )


def rate_human_shuffle_reconstructed(request: HttpRequest) -> HttpResponse:
    """Rate reconstructed human shuffle view."""
    sample = Sample.objects.get(pk=request.session["sample_id"])

    if request.method == "POST":
        form = RateReconstructionForm(request.POST)

        if form.is_valid():
            sample.rating_reconstructed_human_quality = form.cleaned_data["quality"]
            sample.rating_reconstructed_human_niceness = form.cleaned_data["niceness"]
            sample.save()
            return redirect("next_reconstruction")

    else:
        form = RateReconstructionForm()
    return render(
        request,
        "04_rate_human_shuffle_reconstructed.html",
        {
            "form": form,
            "sample_id": sample.id,
            "tokenized_story_text": sent_tokenize(sample.story_text),
            "tokenized_human_reconstructed_story": sent_tokenize(sample.llm_reconstructed_human_story),
        },
    )


def rate_random_shuffle_reconstructed(request: HttpRequest) -> HttpResponse:
    """Rate reconstructed random shuffle view."""
    sample = Sample.objects.get(pk=request.session["sample_id"])

    if request.method == "POST":
        form = RateReconstructionForm(request.POST)

        if form.is_valid():
            sample.rating_reconstructed_random_quality = form.cleaned_data["quality"]
            sample.rating_reconstructed_random_niceness = form.cleaned_data["niceness"]
            sample.save()
            return redirect("thank_you")

    else:
        form = RateReconstructionForm()
    return render(
        request,
        "05_rate_random_shuffle_reconstructed.html",
        {
            "form": form,
            "sample_id": sample.id,
            "tokenized_story_text": sent_tokenize(sample.story_text),
            "tokenized_random_reconstructed_story": sent_tokenize(sample.llm_reconstructed_random_story),
        },
    )


def thank_you(request: HttpRequest) -> HttpResponse:
    """Thank-you view."""
    return render(request, "06_thank_you.html")
