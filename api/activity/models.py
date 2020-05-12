from django.db import models
from django.conf import settings


class Review(models.Model):
    title = models.ForeignKey(
        "objects.Title",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Произведение",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Автор отзыва",
    )
    text = models.TextField(verbose_name="текст отзыва")

    SCORE_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    ]
    score = models.PositiveSmallIntegerField(
        verbose_name="оценка произведения", choices=SCORE_CHOICES
    )

    pub_date = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Comment(models.Model):
    review = models.ForeignKey(
        "Review",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Отзыв",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор комментария",
    )
    text = models.TextField(verbose_name="текст комментария")
    pub_date = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
