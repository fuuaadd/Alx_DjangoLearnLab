from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    p= ["books/create", "books/update", "books/delete"]
    path('books/', BookListView.as_view(), name='book-list'),  
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), 
    h= ["from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"]
    ]
