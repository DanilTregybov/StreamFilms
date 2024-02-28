from datetime import date

from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    """Категорії"""
    name = models.CharField("Категорія", max_length=150)
    description = models.TextField("Опис")
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Actor_Director(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    age = models.PositiveSmallIntegerField("Вік", default=0)
    description = models.TextField("Опис")
    image = models.ImageField("Зображення", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актори та режисери"
        verbose_name_plural = "Актори та режисери"

class Genre(models.Model):
    """Жанр"""
    name = models.CharField("Ім'я", max_length=100)
    description = models.TextField("Опис")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"

class Film(models.Model):
    """Фільм"""
    title = models.CharField("Назва", max_length=100)
    tagline = models.CharField("Гасло", max_length=100, default='')
    description = models.TextField("Опис")
    poster = models.ImageField("Постер", upload_to="films/")
    year = models.PositiveSmallIntegerField("Дата виходу", default=2024)
    country = models.CharField("Країна", max_length=30)
    directors = models.ManyToManyField(Actor_Director, verbose_name="режисер",related_name="film_director")
    actors = models.ManyToManyField(Actor_Director, verbose_name="актори", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанри")
    world_premiere = models.DateField("Прем'єра у світі", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="у дол.США")
    fees_USA = models.PositiveIntegerField("Касові збори у США", default=0, help_text="у дол.США")
    fees_World = models.PositiveIntegerField("Касові збори у Світі", default=0, help_text="у дол.США")
    category = models.ForeignKey(Category, verbose_name="категорія", on_delete=models.SET_NULL,null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Чернетка", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("film_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull = True)
    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"

class Films_Shots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Опис")
    image = models.ImageField("Зображення", upload_to="film_shots/")
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name="Фільм")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр з фільму"
        verbose_name_plural = "Кадри з фільму"
class Rating_Star(models.Model):
    """Зірка рейтингу"""
    value = models.SmallIntegerField("Значення", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Зірка рейтингу"
        verbose_name_plural = "Зірки рейтингу"

class Rating(models.Model):
    """Рейтинг"""

    ip = models.CharField("IP адреса", max_length=15)
    star = models.ForeignKey(Rating_Star, on_delete=models.CASCADE,verbose_name="зірка")
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name="фільм")

    def __str__(self):
        return f"{self.star}-{self.film}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    """Відгук"""
    email = models.EmailField()
    name = models.CharField("Ім'я", max_length=100)
    text = models.TextField("Повідомлення", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Батько", on_delete=models.SET_NULL, blank=True, null=True)
    film = models.ForeignKey(Film, verbose_name="фільм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.film}"

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
