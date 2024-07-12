"""Webapp views."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """webapp/index view."""
    context = {
        "test": "test1234",
    }
    return render(request, "01_start_experiment.html", context)
