from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"
 ["from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"]
p = ["books", "books/create", "books/update", "books/delete"]
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allows any user to view, but only authenticated users can modify
    permission_classes = [IsAuthenticatedOrReadOnly]
