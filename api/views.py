from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.models import Review, Comment
from api.serializers import ReviewSerializer, CommentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404('Title', pk=self.kwargs.get('title_id'))
        return title.reviews

    def perform_create(self, serializer):
        title = get_object_or_404('Title', pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        title = get_object_or_404('Title', pk=self.kwargs.get('title_id'))
        return title.comments

    def perform_create(self, serializer):
        title = get_object_or_404('Title', pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
