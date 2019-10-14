from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Characters(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FilmReview(models.Model):
    name = models.CharField(max_length=255)
    premiere = models.DateField()
    review = models.TextField()
    image = models.ImageField()
    image_source = models.URLField()
    description = models.CharField(max_length=700)
    director = models.CharField(max_length=255)
    genre = models.ManyToManyField(Categories)
    performers = models.ManyToManyField(Characters)

    def __str__(self):
        return self.description

    def show_review(self):
        return self.image
