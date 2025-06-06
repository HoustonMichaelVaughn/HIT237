import os

from django import template
from django.conf import settings
from django.templatetags.static import static

# Sources
# https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/
# https://www.w3schools.com/python/ref_string_rsplit.asp
# https://www.w3schools.com/python/python_strings_slicing.asp

register = template.Library()


@register.filter(name="truncate")
def truncate(data, length=120):
    #   Function takes data, length by defualt is set to 120, if data is longer than that
    #   it will slice at length and then split based on the next space, selects the firstout of that array and
    #   concats a '...'
    if len(data) <= length:
        return data
    return data[:length].rsplit(" ", 1)[0] + "..."


@register.filter(name="repsrcset")
def repsrcset(image_title):
    #   Custom filter to generate the source set html info.
    #   uses range to generate widths (Plus one to include stop of range)
    #   Some images vary in resolution so we use os functions to ensure the srcset only includes
    #   images that actually exist.
    width = range(400, 1201, 200)
    base_path = os.path.join(
        settings.BASE_DIR, "mango_pests", "static", "images", "pests", image_title
    )
    srcseturls = []
    for w in width:
        filename = f"{image_title}-{w}w.webp"
        full_path = os.path.join(base_path, filename)
        if os.path.exists(full_path):
            url = static(f"images/pests/{image_title}/{filename}")
            srcseturls.append(f"{url} {w}w")
    return ", ".join(srcseturls)
