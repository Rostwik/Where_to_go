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
        width = obj.picture.width
        max_height = 200
        max_width = width / (height / max_height)
        print(max_width, max_height)

        return format_html('<img src="{}" width="{}" max-height="200"/>', url, max_width)


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
