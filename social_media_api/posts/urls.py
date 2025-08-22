from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from . import views

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:pk>/like/", views.like_post, name="like_post"),
    path("posts/<int:pk>/unlike/", views.unlike_post, name="unlike_post"),
    path('feed/', views.feed_view, name='feed'),
]
