from django.contrib import admin
from .models import Section

class SectionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cr',
    )
    search_fields = (
        'name',
    )
    readonly_fields = (
    )
    filter_horizontal = (
        'students',
    )
    list_filter = ()
    fieldsets = ()

admin.site.register(Section, SectionAdmin)
