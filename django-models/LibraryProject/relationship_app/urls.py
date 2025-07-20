# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import admin_dashboard 
from .views import librarian_dashboard 
from .views import member_dashboard

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
]
