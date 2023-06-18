from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()  # SELECT * FROM movies_movie
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)  # Shortcut for try/except
    return render(request, 'movies/detail.html', {'movie': movie})
