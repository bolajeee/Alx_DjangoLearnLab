from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'templates/book_list.html', {'books': books})
