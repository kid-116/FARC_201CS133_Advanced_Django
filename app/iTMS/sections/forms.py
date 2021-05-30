from django import forms
from django.db import models
from django.db.models import fields
from .models import Section

class SectionCreationForm(models.ModelForm):
    class Meta:
        model = Section
        fields = [
            'name',
            'students',
            'cr',
        ]
    def clean(self):
        super(SectionCreationForm, self).clean()
        students = self.cleaned_data.get('students')
        cr = self.cleaned_data.get('cr')
        if cr not in students:
            self._errors['cr'] = self.error_class(['CR must belong to the section!'])
        return self.cleaned_data