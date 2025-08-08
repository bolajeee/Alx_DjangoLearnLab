from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList, CustomAuthToken

router = DefaultRouter()
router.register('books_all', BookViewSet, basename='books_all')

urlpatterns = [
    path('', include(router.urls)),  # Router URLs for BookViewSet (CRUD)
    path('books/', BookList.as_view(), name='book-list'),  # Read-only list
    path('api/token/', CustomAuthToken, name='api_token_auth'), # Authentication token
  
]