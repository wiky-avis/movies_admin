from django.contrib import admin

from .models import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = (
        "name",
        "id",
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
    )
    search_fields = (
        "full_name",
        "id",
    )


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork
    extra = 1


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork
    extra = 1


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (
        GenreFilmworkInline,
        PersonFilmworkInline,
    )
    list_display = (
        "title",
        "type",
        "creation_date",
        "rating",
    )
    list_filter = (
        "type",
        "creation_date",
        "rating",
        "genres",
        "persons",
    )
    search_fields = (
        "title",
        "description",
        "id",
    )
