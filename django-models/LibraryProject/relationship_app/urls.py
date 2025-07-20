# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
