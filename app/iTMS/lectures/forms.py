from django import forms
from django.db.models import fields
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