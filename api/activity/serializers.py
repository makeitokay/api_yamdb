from rest_framework import serializers

from api.activity.models import Review, Comment


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


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ("id", "text", "author", "pub_date")
        model = Comment
        read_only_fields = (
            "author",
            "pub_date",
        )
