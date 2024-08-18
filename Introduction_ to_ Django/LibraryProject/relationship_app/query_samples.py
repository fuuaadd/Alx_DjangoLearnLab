import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

if __name__ == "__main__":
    print("Books by Author:", books_by_author("Author Name"))
    print("Books in Library:", books_in_library("Library Name"))
    print("Librarian for Library:", librarian_for_library("Library Name"))
