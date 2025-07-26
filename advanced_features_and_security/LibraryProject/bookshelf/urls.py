# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from .views import admin_dashboard, librarian_dashboard, member_dashboard

urlpatterns = [
    path('books/', list_books, name='book_list'),
]
