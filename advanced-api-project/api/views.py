from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ------------------------
# LIST VIEW
# ------------------------
class BookListView(generics.ListAPIView):
    """
    GET: Returns a list of all books.
    Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


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
