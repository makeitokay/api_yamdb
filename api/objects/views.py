from rest_framework import mixins, viewsets
from rest_framework import filters

from api.objects import serializers
from api.objects.filters import TitleFilter
from api.objects.models import Category, Genre, Title
from api.objects.permissions import (
    TitlePermissions,
    GenrePermissions,
    CategoryPermissions,
)


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (CategoryPermissions,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["=slug", "name"]
    lookup_field = "slug"


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = (GenrePermissions,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["=slug", "name"]
    lookup_field = "slug"


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = serializers.TitleSerializer
    permission_classes = (TitlePermissions,)
    filterset_class = TitleFilter
