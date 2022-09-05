from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, Image


class PlaceInline(admin.TabularInline):
    model = Image
    ordering = ['position']
    extra = 0
    readonly_fields = ['get_preview']
    fields = ('picture', 'get_preview', 'position')

    def get_preview(self, obj):
        url = obj.picture.url
        width = obj.picture.width
        height = obj.picture.height
        height_proportion = height / 200

        if height_proportion > 1:
            height = 200
            width = width / height_proportion

        return format_html(
            mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
                url=url,
                width=width,
                height=height,
            )
            )
        )


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
