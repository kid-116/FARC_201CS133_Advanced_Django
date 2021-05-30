from django.db import models
from django.db.models.fields import TimeField
from sections.models import Section

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    starts_at = models.DateTimeField(blank=False, null=False)
    ends_at = models.DateTimeField(blank=True, null=True)
    venue = models.CharField(max_length=30, blank=False, null=False)
    desc = models.CharField(max_length=100, blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey(Section, blank=False, on_delete=models.CASCADE, null=False, related_name='events')

class Period(models.Model):
    DAYS = (
        (1, 'MONDAY'),
        (2, 'TUESDAY'),
        (3, 'WEDNESDAY'),
        (4, 'THURSDAY'),
        (5, 'FRIDAY'),
        (6, 'SATURDAY'),
        (7, 'SUNDAY')
    )
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=30, blank=False, null=False)
    starts_at = models.TimeField(blank=False, null=False)
    ends_at = models.TimeField(blank=False, null=False)
    venue = models.CharField(max_length=30,blank=True, null=True)
    day = models.PositiveSmallIntegerField(choices=DAYS)
    section = models.ForeignKey(Section, blank=False, null=False, on_delete=models.CASCADE, related_name='periods')

