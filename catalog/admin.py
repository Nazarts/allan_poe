from django.contrib import admin
from .models import FilmReview, Categories, Characters
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class FilmRevAdmin(SummernoteModelAdmin):
    summernote_fields = ('review',)
    list_display = ('name', 'director',)


admin.site.register(FilmReview, FilmRevAdmin)
admin.site.register(Characters)
admin.site.register(Categories)
