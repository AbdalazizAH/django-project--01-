from django.http import HttpResponse
from django.shortcuts import render


from .models import Movie

def movies(request):
    data=Movie.objects.all()
    return render(request, "movies/movies.html", {"movies": data})  # somedata

def home(request):
    return HttpResponse("hello world")


def detail(request ,id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {"movie": data})

def add(request ):
    title = request.POST.get("title")
    year = request.POST.get("year")
    return render(request, "movies/add.html")
