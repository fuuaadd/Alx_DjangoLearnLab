from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view, RegisterView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path(path('register/', RegisterView.as_view(), name='register'), RegisterView.as_view(), name='register'),
]
