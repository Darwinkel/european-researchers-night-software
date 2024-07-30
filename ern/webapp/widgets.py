from django.forms import CheckboxInput, Select, NumberInput, Textarea


class BootstrapCheckboxInput(CheckboxInput):
    template_name = "widgets/bootstrap_checkbox.html"

class BootstrapSelectInput(Select):
    template_name = "widgets/bootstrap_select.html"

class BootstrapIntegerInput(NumberInput):
    template_name = "widgets/bootstrap_integer.html"

class BootstrapTextAreaInput(Textarea):
    template_name = "widgets/bootstrap_textarea.html"