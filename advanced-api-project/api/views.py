from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Fix the import statements for filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters  # Renamed to avoid confusion

# Then in your BookListView, make sure you're using the correctly imported filters
class BookListView(generics.ListAPIView):
    """
    GET: Returns a list of all books.
    Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Add filter backends with correct imports
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Fields that can be filtered
    filterset_fields = ['publication_year', 'author']
    
    # Fields that can be searched
    search_fields = ['title']
    
    # Fields that can be ordered
    ordering_fields = ['title', 'publication_year', 'author__name']
    
    # Default ordering
    ordering = ['publication_year']
# ------------------------
# DETAIL VIEW
# ------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single book by ID.
    Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ------------------------
# CREATE VIEW
# ------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ------------------------
# UPDATE VIEW
# ------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ------------------------
# DELETE VIEW
# ------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book from the database.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
