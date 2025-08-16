from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q


from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PostForm, CommentForm
from .models import Post, Comment

# --- Authentication views (login/logout) via Django's built-ins:
class BlogLoginView(LoginView):
    template_name = 'registration/login.html'     # uses auth system
    redirect_authenticated_user = True

class BlogLogoutView(LogoutView):
    template_name = 'registration/logout.html'

# --- Registration
def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # password hashed by the form
            login(request, user)  # log in immediately after registration
            messages.success(request, 'Welcome! Your account has been created.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# --- Profile view (view + edit)
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'registration/profile.html', context)

# Search posts by title or content FBV
# def search_posts(request):
#     query = request.GET.get('q', '')
#     results = []
#     if query:
#         results = Post.objects.filter(
#             Q(title__icontains=query) |
#             Q(content__icontains=query) 
#             Q(tags__name__icontains=query)  # if using ManyToMany
#         ).distinct()
#     return render(request, 'blog/search_results.html', {'results': results, 'query': query})

class PostSearchView(ListView):
    model = Post
    template_name = "search_results.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.none()  # return empty if no query

class PostByTagListView(ListView):
    model = Post
    template_name = "blog/posts_by_tag.html"
    context_object_name = "posts"

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag_slug")
        return Post.objects.filter(tags__name=tag_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("tag_slug")
        return context


# --- Blog Post CRUD Views ---
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# ---Comments Url---


class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author_id == self.request.user.id

 
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    # HOOK: run after form is valid, before redirect
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_pk'])
        return super().form_valid(form)

    # HOOK: where to go next
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_pk']})

class CommentUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})