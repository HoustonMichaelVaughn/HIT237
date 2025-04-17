from django import template

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
