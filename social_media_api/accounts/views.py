from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, LoginSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Post
from rest_framework.views import APIView

User = get_user_model()
CustomUser = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user_id": user.id,
            "username": user.username,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user_id": user.id,
            "username": user.username,
            "token": token.key
        }, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            "user_id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
        })


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        if request.user == target_user:
            return Response({"error": "You cannot follow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target_user)
        return Response({"message": f"You are now following {target_user.username}."})


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        if request.user == target_user:
            return Response({"error": "You cannot unfollow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target_user)
        return Response({"message": f"You have unfollowed {target_user.username}."})

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # get posts from users the current user follows
        followed_users = self.request.user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by("-created_at")

# List all users (this is where CustomUser.objects.all() comes in)
def list_users(request):
    users = CustomUser.objects.all().values("id", "username", "email")
    return JsonResponse(list(users), safe=False)

@csrf_exempt
@require_POST
def follow_user(request, user_id):
    current_user = request.user
    target_user = get_object_or_404(CustomUser, id=user_id)
    current_user.follow(target_user)
    return JsonResponse({"message": f"You are now following {target_user.username}"})

@csrf_exempt
@require_POST
def unfollow_user(request, user_id):
    current_user = request.user
    target_user = get_object_or_404(CustomUser, id=user_id)
    current_user.unfollow(target_user)
    return JsonResponse({"message": f"You unfollowed {target_user.username}"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=["post"])
    def follow(self, request, pk=None):
        user_to_follow = get_object_or_404(CustomUser, pk=pk)
        request.user.follow(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def unfollow(self, request, pk=None):
        user_to_unfollow = get_object_or_404(CustomUser, pk=pk)
        request.user.unfollow(user_to_unfollow)
        return Response({"message": f"You unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)