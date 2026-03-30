from django import forms

from educational_facilities.models import EducationalFacility
from options.models import Options
from tasks.models import Task


class TaskFormForPrinting(forms.Form):
    educational_facility = forms.ModelChoiceField(EducationalFacility.objects.order_by("short_name").all())
    task = forms.ModelChoiceField(Task.objects.order_by("pk").values_list('id', flat=True))
    what_to_print = forms.ChoiceField(choices=[("front", "Титульный лист"), ("content", "Содержимое"),])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        options = Options.objects.first()

        if options:
            self.fields['educational_facility'].initial = options.educational_facility