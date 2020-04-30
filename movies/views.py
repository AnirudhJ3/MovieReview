from django.shortcuts import render, get_object_or_404

from .models import Movie

# Create your views here.
def index(request):
    
    movies = Movie.objects.all()

    return render(request, 'index.html', {'movies' : movies})