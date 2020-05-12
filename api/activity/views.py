from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.activity import serializers
from api.activity.models import Review
from api.activity.permissions import ReviewPermissions, CommentPermissions
from api.objects.models import Title


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, ReviewPermissions)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get("title_id")
        if Review.objects.filter(author=self.request.user, title_id=title_id).exists():
            raise ValidationError("Review already exists")
        title = get_object_or_404(Title, pk=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, CommentPermissions)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get("review_id"),
            title__id=self.kwargs.get("title_id"),
        )
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get("review_id"))
        serializer.save(author=self.request.user, review=review)
