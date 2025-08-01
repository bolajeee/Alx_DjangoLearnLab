from rest_framework import serializers
from .models import Book

# This serializer will convert Book model instances to JSON format and vice versa.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
