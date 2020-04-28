from django.db import models
from django.conf import settings


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
