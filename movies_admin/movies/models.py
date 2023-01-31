import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True, default="")

    class Meta:
        db_table = "genre"
        verbose_name = _("genre")
        verbose_name_plural = _("genres")
        unique_together = (("name",),)
        ordering = ("name",)

    def __str__(self):
        return self.name


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_("full_name"), max_length=255)

    class Meta:
        db_table = "person"
        verbose_name = _("person")
        verbose_name_plural = _("persons")
        ordering = ("full_name",)

    def __str__(self):
        return self.full_name


class Filmwork(UUIDMixin, TimeStampedMixin):
    class Types(models.TextChoices):
        MOVIE = "movie", _("movie")
        TV_SHOW = "tv_show", _("tv_show")

    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), blank=True, default="")
    creation_date = models.DateField(_("creation_date"), blank=True, null=True)
    rating = models.FloatField(
        _("rating"),
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    type = models.CharField(
        _("type"), max_length=7, choices=Types.choices, default=Types.MOVIE
    )
    genres = models.ManyToManyField(
        Genre, through="GenreFilmwork", verbose_name=_("genres")
    )
    persons = models.ManyToManyField(
        Person, through="PersonFilmwork", verbose_name=_("persons")
    )
    file_path = models.FileField(
        _("file"), blank=True, null=True, upload_to="movies/"
    )

    class Meta:
        db_table = "film_work"
        verbose_name = _("Filmwork")
        verbose_name_plural = _("Filmworks")
        unique_together = (("title", "creation_date"),)
        ordering = ("title",)

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    genre = models.ForeignKey(
        "Genre", on_delete=models.CASCADE, verbose_name=_("genre")
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "genre_film_work"
        verbose_name_plural = _("genres")
        unique_together = (("film_work", "genre"),)
        ordering = ("id",)


class PersonFilmwork(UUIDMixin):
    class Roles(models.TextChoices):
        DIRECTOR = "director", _("director")
        WRITER = "writer", _("writer")
        ACTOR = "actor", _("actor")

    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    person = models.ForeignKey(
        "Person", on_delete=models.CASCADE, verbose_name=_("person")
    )
    role = models.CharField(
        _("role"), max_length=8, choices=Roles.choices, default=Roles.ACTOR
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "person_film_work"
        verbose_name_plural = _("persons")
        unique_together = (("film_work", "person", "role"),)
        ordering = ("id",)
