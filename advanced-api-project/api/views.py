from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters  # Correct import for Django Filter
from django_filters.rest_framework import DjangoFilterBackend  # Import the DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer
["filters.OrderingFilter"]
["filters.SearchFilter"]
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
