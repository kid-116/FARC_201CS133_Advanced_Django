from django.contrib import admin
from .models import Timetable, Event, Period

class TimetableAdmin(admin.ModelAdmin):
    list_display = (
        'section',
    )
    search_fields = ()
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Timetable, TimetableAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Event, EventAdmin)

class PeriodAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Period, PeriodAdmin)
