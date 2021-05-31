from django.db import models
from sections.models import Section

class Days(models.TextChoices):
    MONDAY = 'Monday', 'M'
    TUESDAY = 'Tuesday', 'TU'
    WEDNESDAY = 'Wednesday', 'W'
    THURSDAY = 'Thursday', 'TH'
    FRIDAY = 'Friday', 'FR'
    SATURDAY = 'Saturday', 'SA'
    SUNDAY = 'Sunday', 'SU'

class Lecture(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=30, blank=False, null=False)
    starts_at = models.TimeField(blank=False, null=False)
    ends_at = models.TimeField(blank=False, null=False)
    day = models.CharField(max_length=10, choices=Days.choices)
    section = models.ForeignKey(Section, blank=False, null=False, on_delete=models.CASCADE, related_name='lectures')
