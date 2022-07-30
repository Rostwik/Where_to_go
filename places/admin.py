from django.contrib import admin

from .models import Place, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    # search_fields = ('town', 'address')
    # readonly_fields = ['created_at']
    list_display = (
        'title',
    )
    # list_editable = ['new_building']
    # list_filter = ['new_building', 'rooms_number', 'has_balcony']
    # raw_id_fields = ['liked_by']
    # inlines = [OwnerInline]


@admin.register(Image)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
