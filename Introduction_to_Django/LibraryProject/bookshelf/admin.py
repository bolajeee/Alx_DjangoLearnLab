from django.contrib import admin
frmo .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ['title', 'author']
    list_filter = ['publication_year']

admin.site.register(Book, BookAdmin)
