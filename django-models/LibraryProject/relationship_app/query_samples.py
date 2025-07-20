from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Query all books written by a specific author.
    Args:
        author_name (str): The name of the author to query.
    Returns:
        list: A list of book titles by the author, or an error message if the author is not found.
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"No author found with name: {author_name}"

def query_books_in_library(library_name):
    """
    List all books in a specific library.
    Args:
        library_name (str): The name of the library to query.
    Returns:
        list: A list of book titles in the library, or an error message if the library is not found.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"No library found with name: {library_name}"

def query_librarian_for_library(library_name):
    """
    Retrieve the librarian assigned to a specific library.
    Args:
        library_name (str): The name of the library to query.
    Returns:
        str: The name of the librarian, or an error message if the library or librarian is not found.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library) #or  library.librarian
        return librarian.name
    except Library.DoesNotExist:
        return f"No library found with name: {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to {library_name}"

# Example usage for testing
if __name__ == "__main__":
    # These queries assume sample data exists in the database
    print("Books by author 'John Doe':", query_books_by_author("John Doe"))
    print("Books in 'City Library':", query_books_in_library("City Library"))
    print("Librarian for 'City Library':", query_librarian_for_library("City Library"))