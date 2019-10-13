from django.contrib import admin
from .models import FilmReview, Categories, Characters

# Register your models here.


admin.register(FilmReview, Categories, Characters)(admin.ModelAdmin)
