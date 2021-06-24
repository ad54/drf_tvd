from .views import *
from django.urls import path

urlpatterns = [
    path('author/', AuthorAPI.as_view()),
    path('author/<id>/', AuthorAPILookUp.as_view()),
    path('book/', BooksAPI.as_view()),
    path('book/<id>/', BooksAPILookUp.as_view()),
    path('register/', RegisterUser.as_view()),
]
