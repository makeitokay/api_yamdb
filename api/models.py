from django.db import models


class Review(models.Model):
    title = models.ForeignKey('Title', on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='текст отзыва')
    score = models.PositiveSmallIntegerField(verbose_name='оценка произведения')
