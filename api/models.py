from django.conf import settings
from django.db import models


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
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="category",
        verbose_name="Категория произведения"
    )
    genre = models.ManyToManyField(Genre, related_name="genre", verbose_name="Жанр произведения")

    class Meta:
        verbose_name = 'Произведения'
        verbose_name_plural = 'Произведение'

    @property
    def rating(self):
        all_scores = Review.objects.filter(title=self).values_list('score', flat=True)
        return round(sum(all_scores) / len(all_scores), 1) if len(all_scores) != 0 else None


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews"
    )
    text = models.TextField(verbose_name="текст отзыва")
    score = models.PositiveSmallIntegerField(verbose_name="оценка произведения")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)


class Comment(models.Model):
    review = models.ForeignKey(
        "Review", on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField(verbose_name="текст комментария")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

