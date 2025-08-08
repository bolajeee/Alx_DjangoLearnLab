# API Endpoints

## Books
- `GET /api/books/` — List all books (public)
- `POST /api/books/` — Create a book (authenticated)
- `GET /api/books/<id>/` — Retrieve a book by ID (public)
- `PUT /api/books/<id>/` — Update a book (authenticated)
- `PATCH /api/books/<id>/` — Partially update a book (authenticated)
- `DELETE /api/books/<id>/` — Delete a book (authenticated)

## Permissions
- Read operations: Public
- Write operations: Requires authentication
