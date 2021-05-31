from sections.models import Section
from django.db import models
from sections.models import Section

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    starts_at = models.DateTimeField(blank=False, null=False)
    ends_at = models.DateTimeField(blank=False, null=False)
    venue = models.CharField(max_length=100, blank=False, null=False)
    desc = models.TextField(max_length=300, verbose_name="Description", blank=False, null=False)
    section = models.ForeignKey(Section, blank=False, null=True, on_delete=models.CASCADE, related_name='events')
