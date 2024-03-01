from django.urls import path

from . import views

urlpatterns = [
    path("", views.FilmsView.as_view(),),
    path("filter/", views.FilterFilmsView.as_view(), name="filter"),
    path("search/", views.Search.as_view(), name="search"),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/", views.FilmDetailView.as_view(), name="film_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.Actor_DirectorView.as_view(), name="actor_detail"),



]
