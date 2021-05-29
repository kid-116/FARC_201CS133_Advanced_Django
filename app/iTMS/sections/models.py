from django.db import models
from accounts.models import Account

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    students = models.ManyToManyField(Account, related_name='section', blank=True)
    cr = models.ForeignKey(Account, related_name='cr_of', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="CR")
    def __str__(self):
        return self.name


