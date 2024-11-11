# properties/templatetags/custom_tags.py
from django import template

register = template.Library()

@register.simple_tag
def render_stars(rating):
    # Ensure the rating is within the range of 1 to 5
    rating = int(rating)
    stars = ''
    for i in range(1, 6):
        if i <= rating:
            stars += '<i class="fa fa-star"></i>'  # Full star
        else:
            stars += '<i class="fa fa-star-o"></i>'  # Empty star
    return stars
