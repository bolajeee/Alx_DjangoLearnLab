# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from .views import admin_dashboard, librarian_dashboard, member_dashboard

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),

    path('books/add_book/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit_book/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete_book/', views.delete_book, name='delete_book'),
]
