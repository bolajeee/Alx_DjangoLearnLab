from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# --- Authentication views (login/logout) via Django's built-ins:
class BlogLoginView(LoginView):
    template_name = 'templates/registration/login.html'     # uses auth system
    redirect_authenticated_user = True

class BlogLogoutView(LogoutView):
    template_name = 'templates/registration/logout.html'

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
    return render(request, 'templates/registration/register.html', {'form': form})

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
    return render(request, 'templates/registration/profile.html', context)
