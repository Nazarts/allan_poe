from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import SingleObjectMixin

from .models import FilmReview, Categories
from django.db.models import Q
from django.views.generic import TemplateView, ListView



class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"slider_films": FilmReview.objects.all()[3:7],
                        "top_films1": FilmReview.objects.filter(premiere__year=2019)[7:10],
                        "top_films2": FilmReview.objects.all()[10:14]})
        return context


class CatalogFilmReviews(ListView):
    template_name = "reviews.html"
    context_object_name = "films"
    paginate_by = 12

    def get_queryset(self):
        self.categories = get_object_or_404(Categories, slug=self.kwargs.get("slug"))
        return FilmReview.objects.filter(~Q(image=''), categories=self.categories).order_by("-premiere")


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'categories': Categories.objects.all(),
                        'slug': self.categories.slug,
                        'category': self.categories
                        })
        return context


class SingleFilmView(TemplateView):
    template_name = "single.html"

    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(FilmReview, slug=self.kwargs.get('slug'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': self.object.categories.all(),
            'film': self.object,
            'performers': self.object.characters.all()
        })
        return context


