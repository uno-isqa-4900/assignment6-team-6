from rest_framework import serializers
from .models import Genre, Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "author",
            "genre",
            "summary",
            "isbn",
            "price",
            "get_image"
        )


class GenreSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Genre
        fields = (
            "id",
            "name", 
            "get_absolute_url",
            "books",
        )


