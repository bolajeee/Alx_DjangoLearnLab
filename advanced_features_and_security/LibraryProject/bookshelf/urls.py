# relationship_app/urls.py
from django.urls import path
from .views import book_list
from . import views

urlpatterns = [
    path('books/', book_list, name='book_list'),
]
