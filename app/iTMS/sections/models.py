from django.db import models

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    def __str__(self):
        return self.name


