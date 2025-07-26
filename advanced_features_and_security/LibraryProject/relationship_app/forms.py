from django import forms
from .models import Book, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "role")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Create or update the user profile with the selected role
            role = self.cleaned_data["role"]
            UserProfile.objects.update_or_create(user=user, defaults={"role": role})
        return user
