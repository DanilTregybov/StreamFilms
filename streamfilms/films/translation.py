from modeltranslation.translator import register, TranslationOptions
from .models import Category, Actor_Director, Film, Genre, Films_Shots

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Actor_Director)
class Actor_DirectorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Film)
class FilmTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'description', 'country')

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Films_Shots)
class Films_ShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
