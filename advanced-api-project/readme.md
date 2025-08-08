# API Endpoints

## Books
- `GET /api/books/` — List all books (public)
  - Filtering:
    - By publication year: `/api/books/?publication_year=2020`
    - By author ID: `/api/books/?author=1`
    - By year range: `/api/books/?min_year=2000&max_year=2020` (requires custom filter)
    - By author name: `/api/books/?author_name=tolkien` (requires custom filter)
  - Searching:
    - Search in title: `/api/books/?search=python`
  - Ordering:
    - By publication year (ascending): `/api/books/?ordering=publication_year`
    - By title (descending): `/api/books/?ordering=-title`
    - By author name: `/api/books/?ordering=author__name`

- `POST /api/books/` — Create a book (authenticated)
- `GET /api/books/<id>/` — Retrieve a book by ID (public)
- `PUT /api/books/<id>/` — Update a book (authenticated)
- `PATCH /api/books/<id>/` — Partially update a book (authenticated)
- `DELETE /api/books/<id>/` — Delete a book (authenticated)

## Permissions
- Read operations: Public
- Write operations: Requires authentication
```

### Issues to Fix

I noticed a few issues in your current code that need to be fixed:

1. In `serializers.py`, you're using `timezone` but it's not imported. Add this import:

```python api/serializers.py
from django.utils import timezone
```

2. In `models.py`, the `related_name` for Author-Book relationship is set to "book", but it should be "books" to match your AuthorSerializer. Update the model:

```python api/models.py
class Book(models.Model):
    # ...
    author = models.ForeignKey(
        Author,
        related_name="books",  # Changed from "book" to "books"
        on_delete=models.CASCADE
    )
    # ...
```

3. The URLs in your `api/urls.py` don't match the patterns described in your readme.md. Update the URLs:

```python api/urls.py
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]