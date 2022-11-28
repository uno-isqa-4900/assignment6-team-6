from django.urls import path, include
from book import views

urlpatterns = [
        path('latest-books/', views.LatestBooksList.as_view()),
        path('books/<slug:genre_slug>/<slug:book_slug>/', views.BookDetail.as_view()),
        path('books/<slug:genre_slug>/',views.GenreDetail.as_view()),
        path('genre-list/',views.GenreList.as_view()),

        
]