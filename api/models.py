from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)


class Title(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,  blank=True, related_name="category")
    genre = models.ManyToManyField(Genre, related_name="genre")
    rating = models.FloatField(null=True, blank=True)

    
class Review(models.Model):
    title = models.ForeignKey('Title', on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='текст отзыва')
    score = models.PositiveSmallIntegerField(verbose_name='оценка произведения')
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)


class Comment(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name='текст комментария')
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

