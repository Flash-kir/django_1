from django.contrib import admin
from places.models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('preview_image',)


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('preview_image',)
    fields = ('image', 'preview_image', 'position', )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
