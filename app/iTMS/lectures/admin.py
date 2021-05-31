from django.contrib import admin
from .models import Lecture

class LectureAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
    )
    search_fields = ()
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Lecture, LectureAdmin)
