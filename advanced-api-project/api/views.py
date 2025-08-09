from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter


# ------------------------
# LIST + CREATE
# ------------------------
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books (public, with filters).
    POST: Create a new book (authenticated only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter

    search_fields = ['title']
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['publication_year']  # default ordering

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# ------------------------
# RETRIEVE + UPDATE + DELETE
# ------------------------
class BookDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve book by ID (public).
    PUT/PATCH/DELETE: Authenticated only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
