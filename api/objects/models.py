from django.db import models

from api.activity.models import Review


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название категории")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название жанра")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название произведения")
    description = models.CharField(max_length=400, null=True, blank=True, verbose_name="Описание произведения")
    year = models.IntegerField(null=True, blank=True, verbose_name="Год произведения")
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="category",
        verbose_name="Категория произведения"
    )
    genre = models.ManyToManyField(Genre, related_name="genre", verbose_name="Жанр произведения")

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    @property
    def rating(self):
        all_scores = Review.objects.filter(title=self).values_list('score', flat=True)
        return round(sum(all_scores) / len(all_scores), 1) if len(all_scores) != 0 else None