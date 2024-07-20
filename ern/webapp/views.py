"""Webapp views."""
import random
from datetime import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.defaulttags import url

from .forms import ConsentForm, DemographicsForm, StoryForm, ShuffleStoryForm, RateReconstructionForm
from .models import Sample

from nltk.tokenize import sent_tokenize


def index(request: HttpRequest) -> HttpResponse:
    """webapp/index view."""
    if 'sample_id' in request.session:
        del request.session['sample_id']
    return render(request, "00_language.html")

def consent(request: HttpRequest) -> HttpResponse:
    """webapp/index view."""
    if request.method == "POST":

        form = ConsentForm(request.POST)

        if form.is_valid():
            return redirect("demographics")

    else:
        form = ConsentForm()
    return render(request, "01_consent.html", {
        "form": form,
    })

def demographics(request: HttpRequest) -> HttpResponse:
    """webapp/index view."""
    if request.method == "POST":

        form = DemographicsForm(request.POST)

        if form.is_valid():
            sample = Sample(timestamp=datetime.now(), language="nl", sex=form.cleaned_data["sex"], age=form.cleaned_data["age"])
            sample.save()
            request.session['sample_id'] = sample.id
            return redirect("enter_story")

    else:
        form = DemographicsForm()
    return render(request, "01a_enter_demographics.html", {
        "form": form,
    })

def enter_story(request: HttpRequest) -> HttpResponse:
    """webapp/index view."""
    sample = Sample.objects.get(pk=request.session['sample_id'])
    if request.method == "POST":

        form = StoryForm(request.POST)

        if form.is_valid():

            sample.story_text = form.cleaned_data["story_text"]
            sample.save()
            return redirect("shuffle_story")

    else:
        form = StoryForm()
    return render(request, "02_enter_story.html", {
        "form": form,
        "sample_id": sample.id,
    })


def shuffle_story(request: HttpRequest) -> HttpResponse:
    """webapp/index view."""

    ### !!! NOTE !!! ###
    # This UX should probably be such that users can drag and drop sentences to shuffle them.
    # Does this have scientific consequences? The way that humans have to shuffle?
    sample = Sample.objects.get(pk=request.session['sample_id'])

    if request.method == "POST":

        form = ShuffleStoryForm(request.POST)

        if form.is_valid():
            sample.human_shuffled_story = form.cleaned_data["human_shuffled_story"]

            tokenized_human_shuffled_story = sent_tokenize(sample.human_shuffled_story)
            sample.llm_reconstructed_human_story = "An LLM reconstructed the following human shuffle: " + tokenized_human_shuffled_story # TODO

            tokenized_story = sent_tokenize(sample.story_text)
            sample.random_shuffled_story = random.sample(tokenized_story, len(tokenized_story))

            sample.llm_reconstructed_random_story = "An LLM reconstructed the following random shuffle: " + sample.random_shuffled_story # TODO

            sample.save()
            return redirect("rate_human_shuffle_reconstructed")

    else:
        form = ShuffleStoryForm({"human_shuffled_story": sample.story_text})
    return render(request, "03_shuffle_story.html", {
        "form": form,
        "sample_id": sample.id
    })


def rate_human_shuffle_reconstructed(request: HttpRequest) -> HttpResponse:
    """webapp/index view."""

    sample = Sample.objects.get(pk=request.session['sample_id'])

    if request.method == "POST":

        form = RateReconstructionForm(request.POST)

        if form.is_valid():
            sample.rating_reconstructed_human_fluency = form.cleaned_data["fluency"]
            sample.rating_reconstructed_human_flow = form.cleaned_data["flow"]
            sample.rating_reconstructed_human_accuracy = form.cleaned_data["accuracy"]
            sample.save()
            return redirect("rate_random_shuffle_reconstructed")

    else:
        form = RateReconstructionForm()
    return render(request, "04_rate_human_shuffle_reconstructed.html", {
        "form": form,
        "sample_id": sample.id,
        "story_text": sample.story_text,
        "human_reconstructed_story": random.sample(sample.human_shuffled_story, len(sample.human_shuffled_story)) # should be LLM call
    })


def rate_random_shuffle_reconstructed(request: HttpRequest) -> HttpResponse:
    sample = Sample.objects.get(pk=request.session['sample_id'])

    if request.method == "POST":

        form = RateReconstructionForm(request.POST)

        if form.is_valid():
            sample.rating_reconstructed_random_fluency = form.cleaned_data["fluency"]
            sample.rating_reconstructed_random_flow = form.cleaned_data["flow"]
            sample.rating_reconstructed_random_accuracy = form.cleaned_data["accuracy"]
            sample.save()
            return redirect("thank_you")

    else:
        form = RateReconstructionForm()
    return render(request, "05_rate_random_shuffle_reconstructed.html", {
        "form": form,
        "sample_id": sample.id,
        "story_text": sample.story_text,
        "random_reconstructed_story": random.sample(sample.random_shuffled_story, len(sample.random_shuffled_story)) # should be LLM call
    })

def thank_you(request: HttpRequest) -> HttpResponse:
    """webapp/index view."""
    return render(request, "06_thank_you.html")
