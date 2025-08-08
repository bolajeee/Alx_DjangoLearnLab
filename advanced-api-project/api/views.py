from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters


# ------------------------
# BOOK GENERIC VIEWS
# ------------------------

# List all books OR create a new one
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: Returns a list of all books.
    POST: Creates a new book (requires authentication).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']


    # Permissions:
    # - Unauthenticated users can only read (GET).
    # - Authenticated users can also create (POST).
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# Retrieve a single book, update, or delete it
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single book by ID.
    PUT/PATCH: Update a book (requires authentication).
    DELETE: Delete a book (requires authentication).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
