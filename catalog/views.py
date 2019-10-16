from django.shortcuts import render, get_object_or_404
from .models import FilmReview, Categories, Characters
from django.db.models import Q


def home_view(request):
    context = {"slider_films": FilmReview.objects.all()[3:7],
               "top_films1": FilmReview.objects.filter(premiere__year = 2019)[7:10],
               "top_films2": FilmReview.objects.all()[15:19]}
    return render(request, 'home.html', context)


def catalog_view(request, **kwargs):
    slug = kwargs.get("slug")
    categories = Categories.objects.all()
    category = Categories.objects.get(slug=slug)
    films = FilmReview.objects.filter(~Q(image=''), categories=category).order_by('-premiere')[:20]
    context = {'categories': categories,
               'slug': slug,
               'category': category,
               'films': films
               }
    return render(request, 'reviews.html', context)


def single_view(request, **kwargs):
    slug = kwargs.get("slug")
    film = get_object_or_404(FilmReview, slug=slug)
    context = {'film': film,
               "categories": film.categories.all(),
               }
    return render(request, 'single.html', context)
