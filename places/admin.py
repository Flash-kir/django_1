from django.contrib import admin
from places.models import Place, Image
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.utils.html import format_html


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('preview_image',)

    def preview_image(obj):
        return format_html(
            '<img src="{url}" width={width} />'.format(
                url=obj.image.url,
                width=200,
            )
        )


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    extra = 1
    readonly_fields = ('preview_image',)
    fields = ('image', 'preview_image')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
