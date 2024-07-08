"""Custom widgets for the webapp application."""

from django.forms import CheckboxInput, NumberInput, Select, Textarea


class BootstrapCheckboxInput(CheckboxInput):
    """Override for the default checkbox widget to use a Bootstrap-based template."""

    template_name = "widgets/bootstrap_checkbox.html"


class BootstrapSelectInput(Select):
    """Override for the default select widget to use a Bootstrap-based template."""

    template_name = "widgets/bootstrap_select.html"


class BootstrapIntegerInput(NumberInput):
    """Override for the default integer widget to use a Bootstrap-based range slider template."""

    template_name = "widgets/bootstrap_integer.html"


class BootstrapTextAreaInput(Textarea):
    """Override for the default Textarea widget to use a Bootstrap-based template."""

    template_name = "widgets/bootstrap_textarea.html"
