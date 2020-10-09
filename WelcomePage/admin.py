from django.contrib import admin

from .models import Event, Project


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'project')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description')


admin.site.register(Event, EventAdmin)
admin.site.register(Project)
