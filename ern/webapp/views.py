"""Webapp views."""

from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    """webapp/index view."""
    return HttpResponse("Hello, world. You're at the polls index.")
