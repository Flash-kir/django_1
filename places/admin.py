from django.contrib import admin
from places.models import Place, Image
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from places.admin_view_tools import preview_image


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = [preview_image]


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    extra = 1
    readonly_fields = [preview_image]
    fields = ['image', preview_image]


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
