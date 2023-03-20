from django.utils.html import format_html


def image_html_format(url, width=200):
    return format_html(
            '<img src="{}" width={} />',
            url,
            width,
        )
