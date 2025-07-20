from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
frmo django.contrib.auth.forms import UserCreationForm

# Create your views here.
def list_books(request):
    """
    View to list all books in the library.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Detail view for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Home view to render the main page
def home(request):
    return render(request, 'relationship_app/home.html') 

# Login, Logout, and Register views
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('list_books')  # redirect to a valid page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # redirect to a valid page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
