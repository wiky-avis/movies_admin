import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('name', max_length=255)
    description = models.TextField('description', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Filmwork(models.Model):
    class Types(models.TextChoices):
        MOVIE = 'movie', _('Фильм')
        TV_SHOW = 'tv_show', _('Телешоу')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    creation_date = models.DateField('creation_date')
    rating = models.FloatField('rating')
    type = models.CharField(max_length=7, choices=Types.choices, default=Types.MOVIE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
