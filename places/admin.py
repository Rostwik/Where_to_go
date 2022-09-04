from django.contrib import admin

from .models import Place, Image


class PlaceInline(admin.TabularInline):
    model = Image
    ordering = ['position']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceInline,
    ]
    list_display = (
        'id', 'title',
    )


@admin.register(Image)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'position', 'place'
    )
    ordering = ['place', 'position']
