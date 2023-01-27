from django.contrib import admin

from .models import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
    search_fields = (
        "id",
        "name",
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "id",
    )
    search_fields = (
        "id",
        "full_name",
    )


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork
    extra = 1


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork
    extra = 1
    autocomplete_fields = ("person",)


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (
        GenreFilmworkInline,
        PersonFilmworkInline,
    )
    list_display = (
        "id",
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
    )
    search_fields = (
        "title",
        "description",
        "id",
        "persons",
    )
    list_display_links = ("title",)
