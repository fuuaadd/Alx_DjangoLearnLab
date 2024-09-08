from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

class BookAPITests(APITestCase):
    
    def setUp(self):
        self.author = Author.objects.create(name='J.K. Rowling')
        self.book = Book.objects.create(
            title='Harry Potter',
            publication_year=1997,
            author=self.author
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.book_list_url = reverse('book-list')

    # Test: Create a new book
    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, "New Book")

    # Test: Retrieve a book by ID
    def test_retrieve_book(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    # Test: Update a book
    def test_update_book(self):
        data = {
            "title": "Harry Potter and the Philosopher's Stone",
            "publication_year": 1997,
            "author": self.author.id
        }
        response = self.client.put(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Philosopher's Stone")

    # Test: Delete a book
    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Test: Ensure permissions are working (CreateView restricted to authenticated users)
    def test_create_book_permission(self):
        self.client.logout()  # Ensuring the user is unauthenticated
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
