from django.contrib import admin
from places.models import Place, Image
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.utils.html import format_html


def image_html_format(url, width=200):
    return format_html(
            '<img src="{}" width={} />',
            url,
            width,
        )


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return image_html_format(obj.image.url)


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    extra = 1
    readonly_fields = ['preview_image']
    fields = ['image', 'preview_image']

    def preview_image(self, obj):
        return image_html_format(obj.image.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
