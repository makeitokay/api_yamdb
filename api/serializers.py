from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import Comment, Review, Category, Genre, Title

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name", "slug"]
        model = Category
        lookup_field = "slug"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name", "slug"]
        model = Genre
        lookup_field = "slug"


class GenreField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = GenreSerializer(value)
        return serializer.data


class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = CategorySerializer(value)
        return serializer.data


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreField(
        slug_field="slug", required=False, many=True, queryset=Genre.objects.all()
    )
    category = CategoryField(
        slug_field="slug", required=False, queryset=Category.objects.all()
    )

    class Meta:
        fields = ["name", "year", "category", "genre", "rating", "description", "id"]
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = (
            "id",
            "text",
            "author",
            "score",
            "pub_date",
        )
        model = Review
        read_only_fields = (
            "author",
            "pub_date",
        )

    def validate_score(self, value):
        if value > 10 or value < 1:
            raise serializers.ValidationError("Invalid score")
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ("id", "text", "author", "pub_date")
        model = Comment
        read_only_fields = (
            "author",
            "pub_date",
        )
