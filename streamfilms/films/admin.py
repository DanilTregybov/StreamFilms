from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.gis import forms
# Register your models here.
from .models import Category, Genre, Film, Films_Shots, Actor_Director, Rating, Rating_Star, Reviews

from ckeditor_uploader.widgets import CKEditorUploadingWidget



class FilmAdminForm(forms.ModelForm):
    description = forms.CharField(label="Опис", widget=CKEditorUploadingWidget())

    class Meta:
        model = Film
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url",)
    list_display_links = ("name",)

    # StackedInline


class ReviewInline(admin.TabularInline): #StackedInline
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email",)

class MovieShotsInline(admin.TabularInline):
    model = Films_Shots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "100" height = "110" >')

    get_image.short_description = "Зображення"

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft",)
    list_filter = ("category", "year")
    search_fields = ("title", "category__name",)
    inlines = [MovieShotsInline, ReviewInline ]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["published", "unpublished"]
    readonly_fields = ("get_image",)
    form = FilmAdminForm
    # fields = (("actors", "directors", "genres"),) для фільтрування видимих полів
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"),)
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            # "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_USA", "fees_World"),)
        }),
        (None, {
            "fields": (("url", "draft"),)
        }),

    )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width = "100" height = "110" >')

    get_image.short_description = "Постер"

    def unpublished(self,request,queryset): #знятий з публикації
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запис був ононвлений"
        else:
            message_bit = f"{row_update} записів було ононвлено"
        self.message_user(request, f"{message_bit}")

    def published(self,request,queryset): #опубликаваний
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запис був ононвлений"
        else:
            message_bit = f"{row_update} записів було ононвлено"
        self.message_user(request, f"{message_bit}")

    published.short_description = "Публікувати"
    published.allowed_permissions = ('change',)

    unpublished.short_description = "Знятий з публикації"
    unpublished.allowed_permissions = ('change',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "film", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(Actor_Director)
class Actor_DirectorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "50" height = "60" >')

    get_image.short_description = "Зображення"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("film", "star", "ip")


@admin.register(Films_Shots)
class Films_ShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "film", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "60" height = "60" >')

    get_image.short_description = "Зображення"


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Film)
# admin.site.register(Reviews)
# admin.site.register(Genre)
# admin.site.register(Films_Shots)
# admin.site.register(Actor_Director)
# admin.site.register(Rating)
admin.site.register(Rating_Star)

admin.site.site_title = "Django Films"
admin.site.site_header = "Django Films"
