from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, status, viewsets, views
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from api import serializers
from api.models import Comment, Review
from api.permissions import ReviewPermissions, CommentPermissions, UserPermissions, DenyRoleChanging
from api.serializers import CommentSerializer, ReviewSerializer

from .filters import TitleFilter
from .models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


User = get_user_model()


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["=slug", "name"]
    lookup_field = "slug"

    def get_permissions(self):
        if self.action in ('list',):
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated, IsAdminUser,)
        return [permission() for permission in permission_classes]


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["=slug", "name"]
    lookup_field = "slug"

    def get_permissions(self):
        if self.action in ('list',):
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated, IsAdminUser,)
        return [permission() for permission in permission_classes]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filterset_class = TitleFilter

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated, IsAdminUser,)
        return [permission() for permission in permission_classes]
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated, UserPermissions, )
    lookup_field = 'username'


class UserSelfView(views.APIView):   
    permission_classes = (IsAuthenticated, DenyRoleChanging, )

    def get(self, request):
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data)
    
    def patch(self, request):
        serializer = serializers.UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)    


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (ReviewPermissions, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (CommentPermissions, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'), title__id=self.kwargs.get('title_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get("review_id"))
        serializer.save(author=self.request.user, review=review)