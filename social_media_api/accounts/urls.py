from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView, FeedView
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
