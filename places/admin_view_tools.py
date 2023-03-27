from django.utils.html import format_html


def image_html_format(url, height=200):
    return format_html(
            '<img src="{}" height={} />',
            url,
            height,
        )


def preview_image(self):
    return image_html_format(self.image.url)
