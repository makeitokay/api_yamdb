from rest_framework import filters, mixins, status, viewsets

# TODO: fix imports
from .models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer
from .filters import TitleFilter
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from api import serializers
from api.permissions import IsAdminOrOwner
from rest_framework import viewsets

from api.models import Review, Comment
from api.serializers import ReviewSerializer, CommentSerializer


class CategoryViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=slug', 'name']
    lookup_field = 'slug'


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=slug', 'name']
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filterset_class = TitleFilter

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializert
    pagination_class = PageNumberPagination
    lookup_field = 'username'

    def get_permissions(self):
        if self.action in ('list', 'create'):
            permission_classes = (IsAuthenticated, IsAdminUser,)
        elif self.action in ('retrieve', 'update', 'partial_update', 'destroy'):
            permission_classes = (IsAuthenticated, IsAdminOrOwner)
        return [permission() for permission in permission_classes]

    def retrieve(self, request, username=None):
        if username == 'me':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        return super().retrieve(request, username)

    def partial_update(self, request, username=None, *args, **kwargs):
        if username == 'me':
            user = request.user
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, username=None, *args, **kwargs):
        if username == 'me':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


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

