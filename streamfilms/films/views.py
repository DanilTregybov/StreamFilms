from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Film, Category, Actor_Director, Genre
from .forms import ReviewForm

# class FilmsView(View):
#
#     def get(self, request):
#         films = Film.objects.all()
#         return render(request, "films/film_list.html", {"films_list": films})

class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Film.objects.filter(draft=False).values("year")
class FilmsView(GenreYear, ListView): # Список фільмів
    model = Film
    queryset = Film.objects.filter(draft=False)
    template_name = "films/film_list.html"

class FilmDetailView(GenreYear, DetailView): # Опис фільміу
    model = Film
    slug_field = "url"

class AddReview(GenreYear,View): # Відгуки

    def post(self,request,pk):
       form = ReviewForm(request.POST)
       film = Film.objects.get(id=pk)
       if form.is_valid():
           form = form.save(commit=False)
           if request.POST.get("parent", None):
               form.parent_id =int (request.POST.get("parent"))
           form.film = film
           form.save()
       return redirect(film.get_absolute_url())

class Actor_DirectorView(GenreYear,DetailView):
    model = Actor_Director
    template_name = 'films/actor.html'
    slug_field = "name"

class FilterFilmsView(GenreYear, ListView):

    def get_queryset(self):
        queryset = Film.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset