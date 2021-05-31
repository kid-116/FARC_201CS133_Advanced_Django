from django import forms
from .models import Lecture

class LectureCreationForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = [
            'subject',
            'day',
            'starts_at',
            'ends_at',
        ]
        widgets = {
            'starts_at': forms.TimeInput(attrs={ 'type': 'time' }),
            'ends_at': forms.TimeInput(attrs={ 'type': 'time' }),
        }
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('starts_at') >= cleaned_data.get('ends_at'):
            self.add_error('ends_at', 'Time interval is invalid!')