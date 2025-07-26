from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import BookSearchForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()
    if form.is_valid():
        query = form.cleaned_data.get('title')
        if query:
            books = books.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
