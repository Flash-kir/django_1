from django.utils.html import format_html


def preview_image(self, height=200):
    return format_html(
        '<img src="{}" height={} />',
        self.image.url,
        height,
    )
