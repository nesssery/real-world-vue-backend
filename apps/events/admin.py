from django.contrib import admin
from apps.events.models import Event
from apps.events.models import Categorie


class EventsAdmin(admin.ModelAdmin):
    fields = ('category', 'title', 'location',
              'description', 'organizer',
              'date', 'time')
    list_display = ('id', 'category', 'title', 'location', 'date', 'time')


admin.site.register(Event, EventsAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    fields = ('title', 'description',
              'date', 'time')
    list_display = ('id', 'title', 'description', 'date', 'time')


admin.site.register(Categorie, CategoriesAdmin)
