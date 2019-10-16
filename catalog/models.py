from django.db import models


# Create your models here.
from slugify import slugify


class Categories(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, default="none")

    def __str__(self):
        return self.name


class Characters(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, default="none")

    def __str__(self):
        return self.name


class FilmReview(models.Model):
    name = models.CharField(max_length=255)
    premiere = models.DateField()
    review = models.TextField()
    image = models.ImageField(upload_to="film_images")
    image_source = models.URLField()
    description = models.CharField(max_length=700)
    director = models.CharField(max_length=255)
    categories = models.ManyToManyField(Categories)
    characters = models.ManyToManyField(Characters)
    slug = models.CharField(max_length=255, default="none", unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.description

    @staticmethod
    def create(**kwargs):
        categories = kwargs.pop("genre")
        performers = kwargs.pop("performers")
        ob = FilmReview.objects.create(**kwargs)

        if categories:
            for genre in categories:
                cat = dict(name=genre, slug=slugify(genre))
                category, created = Categories.objects.get_or_create(**cat)
                ob.categories.add(category)
                ob.save()

        if performers:
            for actor in performers:
                perf = dict(name=actor,slug=slugify(actor))
                performer, created = Characters.objects.get_or_create(**perf)
                ob.characters.add(performer)
                ob.save()

        return ob
