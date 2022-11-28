from django.shortcuts import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer

# Create your views here.
class LatestBooksList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()[0:4]
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class GenreList(APIView):
        def get(self, request, format=None):
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
            return Response(serializer.data)


class BookDetail(APIView):
    def get_object(self, genre_slug, book_slug):
        try:
            return Book.objects.filter(genre__slug=genre_slug).get(slug=book_slug)
        except Book.DoesNotExist:
            raise Http404
    def get(self, request, genre_slug, book_slug, format=None):
        book = self.get_object(genre_slug, book_slug)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class GenreDetail(APIView):
    def get_object(self, genre_slug):
        try:
            return Genre.objects.get(slug=genre_slug)
        except Book.DoesNotExist:
            raise Http404
    def get(self, request, genre_slug, format=None):
        genre = self.get_object(genre_slug)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

