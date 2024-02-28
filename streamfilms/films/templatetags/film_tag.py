from django import template
from films.models import Category, Film
register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('films/tags/last_film.html')
def get_last_films(count=5):
    films = Film.objects.order_by("id")[:count]
    return {"last_films": films}
