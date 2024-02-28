from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Film, Category
from .forms import ReviewForm

# class FilmsView(View):
#
#     def get(self, request):
#         films = Film.objects.all()
#         return render(request, "films/film_list.html", {"films_list": films})
class FilmsView(ListView): # Список фільмів
    model = Film
    queryset = Film.objects.filter(draft=False)
    template_name = "films/film_list.html"

class FilmDetailView(DetailView): # Опис фільміу
    model = Film
    slug_field = "url"

class AddReview(View): # Відгуки

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
