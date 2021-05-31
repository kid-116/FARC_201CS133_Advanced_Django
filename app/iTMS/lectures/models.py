from django.db import models
from sections.models import Section

DAYS = (
        (1, 'MONDAY'),
        (2, 'TUESDAY'),
        (3, 'WEDNESDAY'),
        (4, 'THURSDAY'),
        (5, 'FRIDAY'),
        (6, 'SATURDAY'),
        (7, 'SUNDAY')
    )

class Lecture(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=30, blank=False, null=False)
    starts_at = models.TimeField(blank=False, null=False)
    ends_at = models.TimeField(blank=False, null=False)
    day = models.PositiveSmallIntegerField(choices=DAYS)
    section = models.ForeignKey(Section, blank=False, null=False, on_delete=models.CASCADE, related_name='lectures')
