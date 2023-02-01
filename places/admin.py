from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class PlaceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ['get_preview']
    fields = ('picture', 'get_preview', 'position')

    def get_preview(self, obj):
        url = obj.picture.url
        height = obj.picture.height
        if height > 200:
            height = 200

        return format_html('<img src="{}" width="auto" height="{}"/>', url, height)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PlaceInline,
    ]
    list_display = (
        'id', 'title',
    )


@admin.register(Image)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'position', 'id',  'place'
    )

    ordering = ['place', 'position']
