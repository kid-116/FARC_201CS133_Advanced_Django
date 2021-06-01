from django import forms
from django.utils.formats import ISO_INPUT_FORMATS
from .models import Event

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'starts_at',
            'ends_at',
            'venue',
            'desc',
        ]
        widgets = {
            'starts_at': forms.DateTimeInput(attrs={ 'placeholder': 'YYYY-MM-DD   HH:MM:SS' }),
            'ends_at': forms.DateTimeInput(attrs={ 'placeholder': 'YYYY-MM-DD   HH:MM:SS' }),
        }
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('starts_at') >= cleaned_data.get('ends_at'):
            self.add_error('ends_at', 'Time interval is invalid!')