from rest_framework import serializers
from .models import Category, Title, Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Category
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Genre
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(slug_field='slug', required=False, many=True, queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug', required=False, queryset=Category.objects.all())

    class Meta:
        fields = ['name', 'year', 'category', 'genre', 'rating', 'description', 'id']
        model = Title
